from celery.schedules import crontab

from .celery import celery_app
from src.tasks.customer_task import check_status_for_task

celery_app.conf.beat_schedule = {
    "check-status-task": {
        "task": "check_status_for_task",
        "schedule": crontab(minute="*")
    }
}
