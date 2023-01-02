from typing import List

from pydantic import AnyHttpUrl
from pydantic import BaseSettings


class Settings(BaseSettings):
    class Config:
        env_file = "../.env"

    PROJECT_NAME: str = "givebox"

    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []


settings = Settings()
