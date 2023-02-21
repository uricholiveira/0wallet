from fastapi import FastAPI

from src.common.containers import Container
from src.routes import routers


def create_app() -> FastAPI:
    container = Container()

    database = container.db()
    database.create_database()

    app = FastAPI()
    app.container = container
    for router in routers:
        app.include_router(router=router)

    return app


app = create_app()
