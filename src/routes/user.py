from typing import List

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from src.common.containers import Container
from src.domain.entities.user import CreateUser, UserResponse
from src.services.user import UserService

router = APIRouter(prefix="/user", tags=["User"])


@router.get("/", response_model=List[UserResponse])
@inject
async def get_users(user_service: UserService = Depends(Provide[Container.user_service])):
    print("asddsads")
    users = await user_service.get_users()
    return users


@router.get("/{user_id}", response_model=UserResponse)
@inject
async def get_user(user_id: int, user_service: UserService = Depends(Provide[Container.user_service])):
    return await user_service.get_user(user_id=user_id)
