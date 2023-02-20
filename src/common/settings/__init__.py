from pydantic import BaseSettings

from src.common.settings.app import ApplicationConfig
from src.common.settings.auth import AuthConfig
from src.common.settings.database import DatabaseConfig
from src.common.settings.util import UtilConfig


class Settings(BaseSettings):
    database: DatabaseConfig = DatabaseConfig()
    app: ApplicationConfig = ApplicationConfig()
    auth: AuthConfig = AuthConfig()
    util: UtilConfig = UtilConfig()


settings = Settings()
