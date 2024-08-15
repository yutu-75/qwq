import logging
from superset import conf
from obs import ObsClient

# obs操作文档
# https://support.huaweicloud.com/sdk-python-devg-obs/obs_22_0100.html

logger = logging.getLogger(__name__)


def obs_put_file(file_name, metadata):
    """
    把文件上传到华为云对象储存服务器上并反回文件url路径
    @param file_name: 文件名字
    @param metadata: 文件流
    @return:
    """
    try:
        bucket_name = conf.get("HUAWEI_BUCKET_NAME")
        # 创建ObsClient实例
        obs_client = ObsClient(
            access_key_id=conf.get("HUAWEI_ACCESS_KEY_ID"),
            secret_access_key=conf.get("HUAWEI_SECRET_ACCESS_KEY"),
            server=conf.get("HUAWEI_SERVER"),
        )

        object_key = conf.get("HUAWEI_IMG_FOLDER_NAME")+file_name

        resp = obs_client.putContent(bucket_name, object_key, content=metadata)

        if resp.status == 200:
            logger.info(f"{file_name} upload successful!")

        # 关闭obsClient
        obs_client.close()
        return resp.get("body").get("objectUrl")
    except Exception as e:
        logger.exception(f"huawei obs error:{e}")
        return ""


