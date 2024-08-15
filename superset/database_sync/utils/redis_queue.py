import json
from superset import conf
from redis import Redis


class RedisQueue(object):
    """
    redis 队列封装
    todo 链接信息配置 广播 其他操作等
    """

    def __init__(self, queue_name='database_sync:'):
        """
        redis_kwargs: 连接信息
        """
        self.__db = Redis(
            host=conf.get("SUPERSET_REDIS_HOST", "127.0.0.1"),
            port=conf.get("SUPERSET_REDIS_PORT", "6379"),
            password=conf.get("SUPERSET_REDIS_PASSWORD", ""),
            db=conf.get("DATABASE_SYNC_QUEUE_REDIS_DB", 15),
        )
        self.key = queue_name

    def size(self):
        """
        获取队列的长度。
        :return:
        """
        return self.__db.llen(self.key)

    def is_empty(self):
        """
        检查队列是否为空。
        :return:
        """
        return self.size() == 0

    def put(self, item):
        """
        将元素放入队列中。如果元素是字典类型，会先将其转换为 JSON 字符串。
        支持dict直接put
        :param item:
        :return:
        """
        if isinstance(item, dict):
            item = json.dumps(item)
        self.__db.rpush(self.key, item)

    def get_with_block_mode(self, is_dict_mode=False, timeout=0):
        """
        阻塞模式，如果队列为空，会一直等待，直到timeout
        获取队列中第一条数据
        is_dict_mode: 是否需要自动load json
        timeout: 超时时间
        """
        item = self.__db.blpop(self.key, timeout=timeout)
        if item:
            # 0是key，1是value
            item = item[1]

        if is_dict_mode:
            try:
                return json.loads(item)
            except:
                return item
        else:
            return item

    def get(self, is_dict_mode=False):
        """
        从队列中获取第一个元素。可以选择是否自动将 JSON 字符串转换为字典。
        is_dict_mode: 是否需要自动load json
        :param is_dict_mode:
        :return:
        """
        item = self.__db.lpop(self.key)

        if is_dict_mode:
            try:
                return json.loads(item)
            except:
                return item
        else:
            return item

    def pub(self, channel, msg):
        """
        向指定的频道发布消息。
        :param channel:
        :param msg:
        :return:
        """
        return self.__db.publish(channel, msg)

    def listen(self, channel):
        """
        监听指定的频道。
        :param channel:
        :return:
        """
        p = self.__db.pubsub()
        p.subscribe(channel)
        return p.listen()

    def clear(self):
        """
        清空队列
        :return:
        """
        self.__db.ltrim(self.key, 1, 0)
        # self.__db.delete(self.key)


if __name__ == '__main__':
    from superset import create_app

    flask_app = create_app()
    with flask_app.app_context():
        redis_client = RedisQueue()
        # redis_client.clear()
        redis_client.put(
            json.dumps(
                {
                    "execute_type": "add",
                    "task_id": 5,
                }
            )
        )

        # data = redis_client.get(is_dict_mode=True)
        # print(data, type(data))
