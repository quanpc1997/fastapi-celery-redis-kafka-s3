import redis
from .cfg import REDIS_URL
# Kết nối đến Redis
redis_client = redis.StrictRedis.from_url(REDIS_URL)

