from functools import lru_cache

from fastapi import FastAPI

import config
from rest.routers import passenger


async def startup_event():
    pass


def shutdown_event():
    pass


def create_app():
    app = FastAPI()

    @lru_cache()
    def get_settings():
        return config.Settings()

    settings = get_settings()

    app.include_router(passenger.router)

    @app.get("/")
    async def read_main():
        return {"msg": "Hello World"}

    app.on_event('startup')(startup_event)
    app.on_event('shutdown')(shutdown_event)

    return app, settings
