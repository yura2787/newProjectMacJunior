from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

router_auth = APIRouter()


@router_auth.post('/login')
async  def user_login(
        data: OAuth2PasswordRequestForm = Depends()
):
    return