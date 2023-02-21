from contextlib import contextmanager, AbstractContextManager
from typing import Generator, Callable

from sqlalchemy import Column, Integer, create_engine
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy import orm
from sqlalchemy.orm import Session, declared_attr

from src.common.settings import settings, DatabaseConfig


class Database:
    def __init__(self, db_config: DatabaseConfig) -> None:
        self._engine = create_engine(db_config.url, echo=True)
        self._session_factory = orm.scoped_session(
            orm.sessionmaker(
                autoflush=db_config.params.auto_flush,
                bind=self._engine,
            ),
        )

    def create_database(self) -> None:
        Base.metadata.create_all(self._engine)

    @contextmanager
    def session(self) -> Callable[..., AbstractContextManager[Session]]:
        session: Session = self._session_factory()
        try:
            yield session
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()


@as_declarative()
class Base:
    id: str = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
    )
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(self) -> str:
        return self.__name__.replace("Model", "")
