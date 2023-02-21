from sqlalchemy import Column, Integer, String

from src.common.database import Base


class User(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    tag = Column(String(5), nullable=False)
