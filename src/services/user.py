from typing import List

from fastapi import HTTPException
from starlette.status import HTTP_404_NOT_FOUND, HTTP_409_CONFLICT

from src.domain.entities.user import CreateUser
from src.domain.models.user import User
from src.repositories.user import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository) -> None:
        self._repository: UserRepository = user_repository

    async def get_users(self) -> List[User]:
        return await self._repository.get_all()

    async def get_user(self, user_id: int) -> User:
        user = await self._repository.get_by_id(user_id)
        if not user:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND)

        return user

    async def get_user_by_filters(self, name: str, tag: str) -> User:
        user = await self._repository.get_by_filters(name=name, tag=tag)
        if not user:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND)

        return user

    async def create_user(self, model: CreateUser) -> User:
        try:
            has_another_user = await self.get_user_by_filters(
                name=model.name, tag=model.tag
            )
            if has_another_user:
                raise HTTPException(status_code=HTTP_409_CONFLICT)

        except HTTPException as ex:
            if ex.status_code == HTTP_404_NOT_FOUND:
                return await self._repository.create(model)
            raise

    async def update_user(self, user_id: int, model: CreateUser) -> User:
        user = await self.get_user(user_id=user_id)
        try:
            has_another_user = await self.get_user_by_filters(
                name=model.name, tag=model.tag
            )
            if has_another_user:
                raise HTTPException(status_code=HTTP_409_CONFLICT)

        except HTTPException as ex:
            if ex.status_code == HTTP_404_NOT_FOUND:
                return await self._repository.update(user=user, model=model)
            raise
