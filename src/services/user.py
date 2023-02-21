from typing import List, Type

from src.domain.models.user import User
from src.repositories.user import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository) -> None:
        self._repository: UserRepository = user_repository

    async def get_users(self) -> List[Type[User]]:
        return self._repository.get_all()

    async def get_user(self, user_id: int) -> Type[User]:
        return self._repository.get_by_id(user_id)
