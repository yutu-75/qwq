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
@Time       : 2023/7/4 15:08
@Author     : Gus
@Software   : PyCharm
@Description:
"""
import oss2

from superset import conf
from oss2.credentials import EnvironmentVariableCredentialsProvider


class AliyunOss(object):

    def __init__(self):
        self.access_key_id = conf["ALY_AK"]
        self.access_key_secret = conf["ALY_SK"]
        self.auth = oss2.Auth(self.access_key_id, self.access_key_secret)
        self.bucket_name = conf["ALY_BUCKET_NAME"]
        self.endpoint = conf["ALY_ENDPOINT"]
        self.protocol_type = conf.get('PROTOCOL_TYPE', 'http')
        self.bucket = oss2.Bucket(self.auth, self.endpoint, self.bucket_name)

    def put_object_and_set_acl_public_read(self, name, data):
        self.bucket.put_object(name, data)
        self.bucket.put_object_acl(name, oss2.OBJECT_ACL_PUBLIC_READ)
        # todo: 正式上线不用兼容多套环境, 可以删除
        if self.protocol_type == 'http':
            return "{}://{}/{}/{}".format(self.protocol_type, self.endpoint, self.bucket_name, name)
        else:
            return "{}://{}.{}/{}".format(self.protocol_type, self.bucket_name, self.endpoint, name)

# if __name__ == '__main__':
#     al_oss = AliyunOss()
#     al_oss.create_bucket()
