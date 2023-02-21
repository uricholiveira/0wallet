from pydantic import BaseModel, Field


class CreateUser(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    tag: str = Field(..., min_length=5, max_length=5)


class UpdateUser(CreateUser):
    ...


class UserResponse(CreateUser):
    class Config:
        orm_mode = True
