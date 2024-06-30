from fastapi import FastAPI


from src.routes.customer import customer_route
from src.routes.ws import ws_route


def create_app():
    app = FastAPI(docs_url="/", redoc_url="/docs")

    app.include_router(customer_route)
    app.include_router(ws_route)

    return app