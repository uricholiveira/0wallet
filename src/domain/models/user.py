import uuid

from sqlalchemy import UUID, Column, String

from src.common.database import Base


class User(Base):
    id: UUID = Column(
        UUID,
        primary_key=True,
        default=uuid.uuid4(),
        nullable=False,
    )
    name = Column(String(50), nullable=False)
    tag = Column(String(5), nullable=False)
