# Celery

Chú ý trong môi trường Windows cần cài thêm Eventlet

**Cách chạy celery:**

- Chạy worker trên 1 Terminal:
```shell
celery -A src.tasks.customer_task worker --loglevel=info -P eventlet
```

- Chạy flower:
```shell
celery -A configs.celery flower --port=5555
```

- Chạy beat task:
```shell
celery -A configs.periodic_beats beat --loglevel=info
```