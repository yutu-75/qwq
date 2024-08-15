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
# -*- coding: utf-8 -*-

"""
@Time       : 2023/7/4 15:19
@Author     : Gus
@Software   : PyCharm
@Description:
"""
import datetime
import logging

from flask import request, Response
from flask_appbuilder.api import expose, safe
from werkzeug.datastructures import FileStorage

from superset import conf
from superset.extensions import event_logger
from flask_appbuilder.security.decorators import permission_name

from superset.huaweicloud_obs.api import obs_put_file
from superset.key_value.utils import get_uuid_namespace
from superset.utils.aliyun_oss import AliyunOss
from superset.utils.decorators import authenticated
from superset.views.base_api import (
    statsd_metrics,
    BaseSupersetApi
)

from pathlib import Path
from superset.key_value.utils import get_new_uuid

logger = logging.getLogger(__name__)


class UploadFileRestApi(BaseSupersetApi):
    resource_name = "file"
    allow_browser_login = True
    class_permission_name = "Dashboard"

    @expose("/upload", methods=["POST"])
    @authenticated()
    @safe
    @statsd_metrics
    @event_logger.log_this_with_context(
        action=lambda self, *args, **kwargs: f"{self.__class__.__name__}.upload",
        log_to_statsd=False,
    )
    @permission_name('read')
    def upload(self) -> Response:
        """上传本地文件到阿里云
        ---
        post:
          requestBody:
            required: true
            content:
              multipart/form-data:
                schema:
                  type: object
                  properties:
                    formData:
                      description: formData对象
                      type: string
                      format: binary
                    file_path:
                      description: 文件路径, 可不填写
                      default: superset/file
                      type: string
          responses:
            200:
              description: Dashboard share added
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      result:
                        type: object
                        properties:
                          url:
                            type: string
            400:
              $ref: '#/components/responses/400'
            401:
              $ref: '#/components/responses/401'
            404:
              $ref: '#/components/responses/404'
            500:
              $ref: '#/components/responses/500'
        """
        form_data = request.files.get("formData", None)
        if not isinstance(form_data, FileStorage):
            return self.response_400('File object not obtained')

        # 默认走阿里云的oss
        oss = conf.get("OBJECT_STORAGE_SERVICE", "aliyun")

        if oss == "aliyun":
            oss = AliyunOss()
            file_path = self.get_file_path()
            file_name = self.get_file_name(form_data)
            result_url = oss.put_object_and_set_acl_public_read(file_path + file_name,
                                                                form_data)
            result_url = result_url.replace("-internal", "")

        elif oss == "huaweicloud":
            file_name = self.get_file_name(form_data)
            result_url = obs_put_file(file_name, form_data)

        else:
            result_url = self.save_file_local(form_data)

        return self.response(200, result={"url": result_url})

    @staticmethod
    def get_file_path():
        return request.form.get("file_path", 'undefined')

    @staticmethod
    def get_file_name(form_data):

        file_type = form_data.filename.split(".")[-1]
        file_name = "/{}-{}.{}".format(
            get_uuid_namespace(form_data.filename),
            str(int(datetime.datetime.now().timestamp() * 1000000)),
            file_type
        )
        return file_name

    @staticmethod
    def save_file_local(form_data):
        img_save_path = Path(__file__).parent.parent.joinpath(
            'static/backend_upload_img'
        )
        if not img_save_path.is_dir():
            img_save_path.mkdir()
        file_name = f"{get_new_uuid()}_{form_data.filename}"
        img_path = str(img_save_path.joinpath(file_name))

        form_data.save(img_path)  # 保存文件到指定路径

        host_url = request.host_url + conf['STATIC_ASSETS_PREFIX'].replace(
            "/", "") + "/" if \
            conf[
                'STATIC_ASSETS_PREFIX'] else request.host_url
        result_url = f"{host_url}static/backend_upload_img/{file_name}"
        return result_url
