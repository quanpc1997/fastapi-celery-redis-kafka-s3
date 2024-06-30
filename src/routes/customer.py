from fastapi import APIRouter, Depends
from celery.result import AsyncResult

from src.service.customer_service import CustomerService
from src.service.repositories.customer_repo import CustomerRepo
from src.tasks.customer_task import export_to_excel
from configs.redis import redis_client
from configs.cfg import PROGRESS_TASK_NAME
from loguru import logger

customer_route = APIRouter(prefix="/customer")

def get_customer_service():
    return CustomerService(CustomerRepo())


def get_redis_client():
    return redis_client


@customer_route.get("/export")
async def to_excel(redis_client=Depends(get_redis_client)):
    task = export_to_excel.delay()
    logger.warning(f"task_id = {task.id}")
    redis_client.lpush(PROGRESS_TASK_NAME, task.id)
    return {"task_id": task.id}


@customer_route.get("/{id}")
async def get_customer(
        id: int,
        customer_service: CustomerService = Depends(get_customer_service)):
    return await customer_service.get_by_id(id)

