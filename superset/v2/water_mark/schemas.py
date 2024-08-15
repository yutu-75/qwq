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
@Time       : 2023/3/28 17:36
@Author     : Gus
@Software   : PyCharm
@Description:
"""
from marshmallow import fields, Schema

# 水印配置
# 文字
WATER_MARK_TEXT = '长安水印logo'
# 颜色(十六进制)
WATER_MARK_COLOR = '#8B8B1B'
# 字体大小
WATER_MARK_SIZE = 30
# 透明度 （0~1）
WATER_MARK_OPACITY = 0.5
# 文字间隔
WATER_MARK_SPACE = 400
# 文字旋转角度（逆时针方向以度为单位）
WATER_MARK_ANGLE = 50
# PDF 宽度
WATER_MARK_PDF_WIDTH = 1200
# PDF 高度
WATER_MARK_PDF_HIGH = 2000


class WaterMarkV2GetSchema(Schema):
    TEXT = fields.String(required=False)
    COLOR = fields.String(required=False)
    SIZE = fields.Int(required=False)
    OPACITY = fields.Float(required=False)
    SPACE = fields.Int(required=False)
    ANGLE = fields.Int(required=False)
    PDF_WIDTH = fields.Int(required=False)
    PDF_HIGH = fields.Int(required=False)


class WaterMarkV2PutSchema(Schema):
    TEXT = fields.String(required=False)
    COLOR = fields.String(required=False)
    SIZE = fields.Int(required=False)
    OPACITY = fields.Float(required=False)
    SPACE = fields.Int(required=False)
    ANGLE = fields.Int(required=False)
    PDF_WIDTH = fields.Int(required=False)
    PDF_HIGH = fields.Int(required=False)
