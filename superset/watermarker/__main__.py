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

import argparse

from watermarker.marker import add_mark


def main():
    parse = argparse.ArgumentParser(description="用于一张图片或一个图片文件夹批量添加水印")
    parse.add_argument("file", type=str, help="图片文件或图片文件夹路径")
    parse.add_argument("mark", type=str, help="要添加的水印内容")
    parse.add_argument("-o", "--out", default="./output", help="添加水印后的结果保存位置，默认生成到output文件夹")
    parse.add_argument("-c", "--color", default="#8B8B1B", type=str, help="水印颜色，默认#8B8B1B")
    parse.add_argument("-s", "--space", default=75, type=int, help="水印直接的间隔, 默认75个空格")
    parse.add_argument("-a", "--angle", default=30, type=int, help="水印旋转角度，默认30度")
    parse.add_argument("--size", default=50, type=int, help="水印字体的大小，默认50")
    parse.add_argument("--opacity", default=0.15, type=float, help="水印的透明度，默认0.15")

    args = parse.parse_args()

    add_mark(args.file, args.mark, args.out, args.color, args.size, args.opacity, args.space, args.angle)


if __name__ == '__main__':
    main()
