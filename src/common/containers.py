from pathlib import Path

from dependency_injector import containers, providers

from src.common.database import Database
from src.common.settings import Settings
from src.repositories.user import UserRepository
from src.services.user import UserService


class Container(containers.DeclarativeContainer):
    path = Path().absolute().joinpath("src/routes")
    modules = ["src.routes." + x.stem for x in path.iterdir()]
    wiring_config = containers.WiringConfiguration(modules=modules)

    settings = Settings()

    db = providers.Singleton(Database, settings.database)

    user_repository = providers.Factory(
        UserRepository, session_factory=db.provided.session
    )
    user_service = providers.Factory(UserService, user_repository=user_repository)
