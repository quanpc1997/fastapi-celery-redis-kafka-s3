from celery import Celery
from .cfg import REDIS_BROKER, REDIS_BACKEND


celery_app = Celery(
    "tasks",
    broker=REDIS_BROKER,
    backend=REDIS_BACKEND
)

# disable UTC so that Celery can use local time
celery_app.conf.enable_utc = False


