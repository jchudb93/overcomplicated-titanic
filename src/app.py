import config
from functools import lru_cache
from fastapi import FastAPI
from rest.routers import passenger

def create_app():

	app = FastAPI()
	app.include_router(passenger.router)

	@lru_cache()
	def get_settings():
		return config.Settings()

	settings = get_settings()

	@app.get("/")
	async def read_main():
		return {"msg": "Hello World"}
	return app, settings