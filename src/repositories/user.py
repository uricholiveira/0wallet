from contextlib import AbstractContextManager
from typing import Callable, List

from sqlalchemy.orm import Session

from src.domain.entities.user import CreateUser
from src.domain.models.user import User


class UserRepository:
    def __init__(
        self, session_factory: Callable[..., AbstractContextManager[Session]]
    ) -> None:
        self.session_factory = session_factory

    async def get_all(self) -> List[User] | None:
        with self.session_factory() as session:
            return session.query(User).all()

    async def get_by_id(self, user_id: int) -> User | None:
        with self.session_factory() as session:
            return session.query(User).filter_by(id=user_id).first()

    async def get_by_filters(
        self,
        user_id: int | None = None,
        name: str | None = None,
        tag: str | None = None,
    ) -> User | None:
        with self.session_factory() as session:
            query = session.query(User)

            if user_id:
                query = query.filter_by(id=user_id)
            if name:
                query = query.filter_by(name=name)
            if tag:
                query = query.filter_by(tag=tag)

            return query.first()

    async def create(self, model: CreateUser) -> User | None:
        user = User(**model.dict())
        with self.session_factory() as session:
            session.add(user)
            session.commit()
            session.refresh(user)

        return user

    async def update(self, user: User, model: CreateUser) -> User | None:
        user.name = model.name
        user.tag = model.tag

        with self.session_factory() as session:
            session.add(user)
            session.commit()
            session.refresh(user)

        return user
