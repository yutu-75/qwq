from cachelib import RedisCache

from superset import conf

cache = RedisCache(
    host=conf.get("SUPERSET_REDIS_HOST"),
    port=conf.get("SUPERSET_REDIS_PORT"),
    password=conf.get("SUPERSET_REDIS_PASSWORD"),
    db=conf.get("SUPERSET_REDIS_DB"),
)
