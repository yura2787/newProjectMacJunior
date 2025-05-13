from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from applications.users.schemas import BaseFields, RegisterUserFields
from database.session_dependenscise import get_async_session
from applications.users.models import User

router_users = APIRouter()

async def create_user_in_db(email, name, password, session):
    new_user = User(email=email, hashed_password=password, name=name)
    session.add(new_user)
    await session.commit()



@router_users.post("/create", status_code=status.HTTP_201_CREATED)
async def create_user(new_user: RegisterUserFields, session: AsyncSession = Depends(get_async_session)) -> BaseFields:
    await create_user_in_db(new_user.email, new_user.name, new_user.password, session)
    return new_user
