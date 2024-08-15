# -*- coding: utf-8 -*-
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""
@Time       : 2023/8/16 13:18
@Author     : Gus
@Software   : PyCharm
@Description:
"""

# -*- coding: utf-8 -*-

"""
@Time       : 2023/6/25 19:03
@Author     : Gus
@Software   : PyCharm
@Description:
"""
from Crypto.Cipher import AES
import base64
import binascii
import time
import json


# 数据处理类
class DataModify:
    def __init__(self, data=b"", characterSet='utf-8'):
        # data必须为bytes类型
        self.data = data
        self.characterSet = characterSet

    def save_data(self, FileName):
        with open(FileName, 'wb') as f:
            f.write(self.data)

    def from_string(self, data):
        self.data = data.encode(self.characterSet)
        return self.data

    def from_base64(self, data):
        self.data = base64.b64decode(data.encode(self.characterSet))
        return self.data

    def from_hexStr(self, data):
        self.data = binascii.a2b_hex(data)
        return self.data

    def to_string(self):
        return self.data.decode(self.characterSet)

    def to_base64(self):
        return base64.b64encode(self.data).decode()
        # return base64.b64encode(self.data)

    def to_hex_str(self):
        return binascii.b2a_hex(self.data).decode()

    def to_bytes(self):
        return self.data

    def __str__(self):
        try:
            return self.to_string()
        except Exception:
            return self.to_base64()


# AES加密类
class AesCryptor:
    def __init__(self, key, mode, iv='', paddingMode="NoPadding", characterSet="utf-8"):
        """
        构建一个AES对象
        key: 秘钥，字节型数据
        mode: 使用模式，只提供两种，AES.MODE_CBC, AES.MODE_ECB
        iv： iv偏移量，字节型数据
        paddingMode: 填充模式，默认为NoPadding, 可选NoPadding，ZeroPadding，PKCS5Padding，PKCS7Padding
        characterSet: 字符集编码
        """
        self.key = key
        self.mode = mode
        self.iv = iv
        self.characterSet = characterSet
        self.paddingMode = paddingMode
        self.data = ""

    def __zero_padding(self, data):
        data += b'\x00'
        while len(data) % 16 != 0:
            data += b'\x00'
        return data

    def __strip_zero_padding(self, data):
        data = data[:-1]
        while len(data) % 16 != 0:
            data = data.rstrip(b'\x00')
            if data[-1] != b"\x00":
                break
        return data

    def __pkcs5_7padding(self, data):
        need_size = 16 - len(data) % 16
        if need_size == 0:
            need_size = 16
        return data + need_size.to_bytes(1, 'little') * need_size

    def __strip_pkcs5_7padding(self, data):
        padding_size = data[-1]
        return data.rstrip(padding_size.to_bytes(1, 'little'))

    def __padding_data(self, data):
        if self.paddingMode == "NoPadding":
            if len(data) % 16 == 0:
                return data
            else:
                return self.__zero_padding(data)
        elif self.paddingMode == "ZeroPadding":
            return self.__zero_padding(data)
        elif self.paddingMode == "PKCS5Padding" or self.paddingMode == "PKCS7Padding":
            return self.__pkcs5_7padding(data)
        else:
            print("不支持Padding")

    def __strip_padding_data(self, data):
        if self.paddingMode == "NoPadding":
            return self.__strip_zero_padding(data)
        elif self.paddingMode == "ZeroPadding":
            return self.__strip_zero_padding(data)

        elif self.paddingMode == "PKCS5Padding" or self.paddingMode == "PKCS7Padding":
            return self.__strip_pkcs5_7padding(data)
        else:
            print("不支持Padding")

    def set_character_set(self, characterSet):
        '''
        设置字符集编码
        characterSet: 字符集编码
        '''
        self.characterSet = characterSet

    def set_padding_mode(self, mode):
        '''
        设置填充模式
        mode: 可选NoPadding，ZeroPadding，PKCS5Padding，PKCS7Padding
        '''
        self.paddingMode = mode

    def decrypt_from_base64(self, entext):
        '''
        从base64编码字符串编码进行AES解密
        entext: 数据类型str
        '''
        mData = DataModify(characterSet=self.characterSet)
        self.data = mData.from_base64(entext)
        return self.__decrypt()

    def decrypt_from_hex_str(self, entext):
        '''
        从hexstr编码字符串编码进行AES解密
        entext: 数据类型str
        '''
        mData = DataModify(characterSet=self.characterSet)
        self.data = mData.from_hexStr(entext)
        return self.__decrypt()

    def decrypt_from_string(self, entext):
        '''
        从字符串进行AES解密
        entext: 数据类型str
        '''
        mData = DataModify(characterSet=self.characterSet)
        self.data = mData.from_string(entext)
        return self.__decrypt()

    def decrypt_from_bytes(self, entext):
        '''
        从二进制进行AES解密
        entext: 数据类型bytes
        '''
        self.data = entext
        return self.__decrypt()

    def encrypt_from_string(self, data):
        '''
        对字符串进行AES加密
        data: 待加密字符串，数据类型为str
        '''
        self.data = data.encode(self.characterSet)
        return self.__encrypt()

    def __encrypt(self):
        if self.mode == AES.MODE_CBC:
            aes = AES.new(self.key, self.mode, self.iv)
        elif self.mode == AES.MODE_ECB:
            aes = AES.new(self.key, self.mode)
        else:
            print("不支持这种模式")
            return

        data = self.__padding_data(self.data)
        enData = aes.encrypt(data)
        return DataModify(enData)

    def __decrypt(self):
        if self.mode == AES.MODE_CBC:
            _aes = AES.new(self.key, self.mode, self.iv)
        elif self.mode == AES.MODE_ECB:
            _aes = AES.new(self.key, self.mode)
        else:
            print("不支持这种模式")
            return
        data = _aes.decrypt(self.data)
        m_data = DataModify(self.__strip_padding_data(data), characterSet=self.characterSet)
        return m_data


def gen_token():
    __data = {"systemKey": "iic_c1cec5d5fe35", "t": (int(time.time() * 1000))}
    key = __data["systemKey"].encode(encoding="utf8")
    iv = key
    aes = AesCryptor(key, AES.MODE_CBC, iv, paddingMode="PKCS5Padding",
                     characterSet='utf-8')
    _data = json.dumps(__data)
    rData = aes.encrypt_from_string(_data)
    return rData.to_base64()


if __name__ == '__main__':
    # key = b"1234567812345678"
    # iv = b"0000000000000000"
    # aes = AesCryptor(key, AES.MODE_CBC, iv, paddingMode="ZeroPadding", characterSet='utf-8')
    #
    # _data = "好好学习"
    # rData = aes.encrypt_from_string(_data)
    # print("密文：", rData.to_base64())
    # rData = aes.decrypt_from_base64(rData.to_base64())
    # print("明文：", rData)

    # __data = {"systemKey": "iic_c1cec5d5fe35", "t": str(time.time())}
    __data = {"systemKey": "iic_c1cec5d5fe35", "t": (int(time.time() * 1000))}
    key = __data["systemKey"].encode(encoding="utf8")
    # key = "iic_c1cec5d5fe35"
    iv = key
    aes = AesCryptor(key, AES.MODE_CBC, iv, paddingMode="PKCS5Padding", characterSet='utf-8')

    # _data = str(__data)
    _data = json.dumps(__data)
    rData = aes.encrypt_from_string(_data)
    # ret = rData.to_base64()
    print("密文：", rData)
    rData = aes.decrypt_from_base64(rData.to_base64())
    # rData = aes.decrypt_from_base64(rData)
    print("明文：", rData)
