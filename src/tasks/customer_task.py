from configs.celery import celery_app
from configs.redis import redis_client
from configs.cfg import PROGRESS_TASK_NAME
import pandas as pd
from celery.result import AsyncResult
import aiohttp


@celery_app.task(bind=True)
def export_to_excel(self):
    try:
        filename = "output.xlsx"
        data = [
            {'Name': 'Alice', 'Age': 30, 'City': 'New York'},
            {'Name': 'Bob', 'Age': 25, 'City': 'Los Angeles'},
            {'Name': 'Charlie', 'Age': 35, 'City': 'Chicago'}
        ]
        df = pd.DataFrame(data)
        # Ghi dữ liệu vào file Excel
        df.to_excel(filename, index=False)
        print(f'Data has been exported to {filename}')

    except Exception as e:
        raise self.retry(exc=e, countdown=60)


@celery_app.task(name='hello')
async def check_status_for_task():
   progress_task_list = redis_client.lrange(PROGRESS_TASK_NAME, 0, -1)
   async for id in progress_task_list:
       if AsyncResult(id).status == "SUCCESS":
            # Xóa task_id trong redis
            redis_client.rlem(PROGRESS_TASK_NAME, id)

            # send id đến cho websocket
            async with aiohttp.ClientSession() as session:
                async with session.ws_connect('ws://localhost:8000/ws') as ws:
                    await ws.send_str(id)
                    await ws.close()


