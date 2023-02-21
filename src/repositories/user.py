from contextlib import AbstractContextManager
from typing import Callable, List, Type

from sqlalchemy.orm import Session

from src.domain.models.user import User


class UserRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def get_all(self) -> List[Type[User]] | None:
        with self.session_factory() as session:
            return session.query(User).all()

    def get_by_id(self, user_id: int) -> Type[User] | None:
        with self.session_factory() as session:
            return session.query(User).filter_by(User.id == user_id).first()
