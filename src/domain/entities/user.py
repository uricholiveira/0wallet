from fastapi import Query
from pydantic import BaseModel, Field
from pydantic.types import UUID


class CreateUser(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    tag: str = Field(..., min_length=5, max_length=5)


class UpdateUser(CreateUser):
    ...


class UserResponse(CreateUser):
    id: UUID = Field(...)

    class Config:
        orm_mode = True


class GetUserParams(BaseModel):
    name: str = Query(..., min_length=3, max_length=50)
    tag: str = Query(..., min_length=5, max_length=5)
