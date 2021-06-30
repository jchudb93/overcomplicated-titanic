from functools import lru_cache
from fastapi import FastApi
from . import config

def create_app():

	app  = FastApi()

	@lru_cache()
	def get_settings():
		return config.Settings()

	settings = get_settings()
	return app, settings