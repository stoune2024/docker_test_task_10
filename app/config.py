from pydantic_settings import BaseSettings, SettingsConfigDict
import os


class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    APP_HOST: str
    APP_HOST_PORT: int
    APP_CONTAINER_PORT: int

    model_config = SettingsConfigDict(
        env_file=f"{os.path.dirname(os.path.abspath(__file__))}/../.env"
    )

    @property
    def database_url(self):
        return f"postgres://{self.POSTGRES_USER}: {self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"


settings = Settings()
