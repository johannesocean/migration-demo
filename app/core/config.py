"""
Created on 2022-12-08 15:19
@author: johannes
"""
from pydantic import BaseSettings

from app import BASE_DIR


class Settings(BaseSettings):
    API_KEY: str
    DB_CONNECTION_STRING: str

    class Config:
        env_file = BASE_DIR.joinpath('.env')


settings = Settings()
