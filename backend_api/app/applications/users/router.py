from fastapi import APIRouter, status

from applications.users.schemas import BaseFields, RegisterUserFields

user_router = APIRouter()


@user_router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_user(new_user: RegisterUserFields) -> BaseFields:
    return new_user
