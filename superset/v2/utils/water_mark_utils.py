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

import base64
import io
import math
import urllib.request

from PIL import Image
from PyPDF2 import PdfReader, PdfWriter
from flask import g
from watermarker.marker import get_mark_img, im_add_mark

from superset import conf
from superset.sys_manager.sys_config.dao import SysConfigDAO
from superset.v2.utils.wkhtmltopdf_utils import wk_to_pdf_binary_by_html


class WaterMark(object):
    def __init__(self, user=None):
        self.TEXT = f"{user.cn_name}: {user.username}" \
            if user else f"{g.user.cn_name}: {g.user.username}"
        self.__init_by_db()

    def __init_by_db(self):
        """
            查询数据库配置，初始化基础参数
        """
        res = SysConfigDAO.find_by_type('WATER_MARK')
        if res:
            res = {item.param_key: item.param_value for item in res}
        else:
            res = {}

        self.COLOR = res.get('COLOR', conf["WATER_MARK_COLOR"])
        self.SIZE = int(res.get('SIZE', conf["WATER_MARK_SIZE"]))
        self.OPACITY = float(res.get('OPACITY', conf["WATER_MARK_OPACITY"]))
        self.SPACE = int(res.get('SPACE', conf["WATER_MARK_SPACE"]))
        self.ANGLE = int(res.get('ANGLE', conf["WATER_MARK_ANGLE"]))
        self.PDF_WIDTH = int(res.get('PDF_WIDTH', conf["WATER_MARK_PDF_WIDTH"]))
        self.PDF_HIGH = int(res.get('PDF_HIGH', conf["WATER_MARK_PDF_HIGH"]))

    def __create_mark_to_pdf_binary(self):
        """
            创建水印pdf对象, 通过水印图片
        """

        im = Image.new(mode='RGBA',
                       size=(self.PDF_WIDTH, self.PDF_HIGH),
                       )
        img = im_add_mark(im=im,
                          text=self.TEXT,
                          color=self.COLOR,
                          size=self.SIZE,
                          opacity=self.OPACITY,
                          space=self.SPACE,
                          angle=self.ANGLE,
                          )
        # 创建io流
        output_buffer = io.BytesIO()
        # 保存img对象
        img.save(output_buffer, format='png')
        byte_data = output_buffer.getvalue()
        # 转换为base64_str
        base64_str = base64.b64encode(byte_data).decode('utf-8')
        base64_str = f'data:image/png;base64,' + base64_str
        html_text = f'<img src="{base64_str}"/>'

        return wk_to_pdf_binary_by_html(html_text)

    def __create_mark_to_img_pil(self):
        """
            创建水印文件对象
        """
        img = get_mark_img(text=self.TEXT,
                           color=self.COLOR,
                           size=self.SIZE,
                           opacity=self.OPACITY,
                           )
        return img

    def __create_mark_by_img_base64_to_img_pil(self, base64_str):
        """
            传入图片 base64——str，并在此添加水印, 返回图片对象
        """
        if base64_str.startswith('data:image/'):
            r = urllib.request.urlopen(base64_str)
            img = Image.open(r.file)
        else:
            byte_data = base64.b64decode(base64_str)
            image_data = io.BytesIO(byte_data)
            img = Image.open(image_data)

        return self.__create_mark_by_img_pil_to_img_pil(
            img,
            self.__create_mark_to_img_pil()
        )

    def __create_mark_by_img_pil_to_img_pil(self, im, mark_img):
        """
            通过图片 加水印 生成图片
        """
        space = self.SPACE
        angle = self.ANGLE
        # 获取水印图片对象
        mark = mark_img
        # 将水印图片扩展并旋转生成水印大图
        w, h = im.size
        c = int(math.sqrt(w ** 2 + h ** 2))
        mark2 = Image.new(mode='RGBA', size=(c, c))
        y, idx = 0, 0
        mark_w, mark_h = mark.size
        while y < c:
            x = -int((mark_w + space) * 0.5 * idx)
            idx = (idx + 1) % 2
            while x < c:
                mark2.paste(mark, (x, y))
                x = x + mark_w + space
            y = y + mark_h + space
        # 将水印大图旋转一定角度
        mark2 = mark2.rotate(angle)
        # 在原图上添加水印大图
        if im.mode != 'RGBA':
            im = im.convert('RGBA')
        im.paste(mark2, (int((w - c) / 2), int((h - c) / 2)),  # 坐标
                 mask=mark2.split()[3])
        return im

    def __add_mark_by_pdf_binary_to_pdf_binary(self, pdf_binary):
        """
            添加pdf水印 通过pdf对象
        """
        pdf_output = PdfWriter()
        pdf_input = PdfReader(io.BytesIO(pdf_binary), strict=False)
        # 获取PDF文件的页数
        page_num = len(pdf_input.pages)

        # 读入水印pdf文件
        pdf_watermark = PdfReader(
            io.BytesIO(self.__create_mark_to_pdf_binary()),
            strict=False
        )

        # 给每一页打水印
        for i in range(page_num):
            page = pdf_input.pages[i]
            page.merge_page(pdf_watermark.pages[0])
            page.compress_content_streams()  # 压缩内容
            pdf_output.add_page(page)

        output_buffer = io.BytesIO()
        pdf_output.write(output_buffer)
        byte_data = output_buffer.getvalue()
        return byte_data

    def __add_mark_by_img_base64_to_img_binary(self, base64_str):
        """
            传入图片base64，并在此添加水印, 返回图片 binary
        """

        img = self.__create_mark_by_img_base64_to_img_pil(base64_str)

        # 创建io流
        output_buffer = io.BytesIO()
        # 保存img对象
        img.save(output_buffer, format='png')
        return output_buffer.getvalue()

    def __add_mark_by_img_base64_to_img_base64(self, base64_str):
        """
            传入图片 base64——str，并在此添加水印, 返回图片base64 str
        """
        img = self.__create_mark_by_img_base64_to_img_pil(base64_str)

        # 创建io流
        output_buffer = io.BytesIO()
        # 保存img对象
        img.save(output_buffer, format='png')
        byte_data = output_buffer.getvalue()
        # 转换为base64_str
        base64_str = base64.b64encode(byte_data).decode('utf-8')
        base64_str = f'data:image/png;base64,' + base64_str
        return base64_str

    def add_mark(self, in_type, in_data, out_type):
        """
            in_type: 输入参数类型
                    img_base64: 图片base64字符串
                    pdf_binary: pdf二进制流
            out_type: 输出参数类型
                    img_base64: 图片base64字符串
                    img_binary: 图片二进制流
                    pdf_binary: pdf二进制流
            in_data: 输入参数
        """

        if in_type == 'img_base64' and out_type == 'img_base64':
            return self.__add_mark_by_img_base64_to_img_base64(in_data)

        if in_type == 'img_base64' and out_type == 'img_binary':
            return self.__add_mark_by_img_base64_to_img_binary(in_data)

        if in_type == 'pdf_binary' and out_type == 'pdf_binary':
            return self.__add_mark_by_pdf_binary_to_pdf_binary(in_data)
