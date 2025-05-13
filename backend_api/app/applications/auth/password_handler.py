from passlib.context import CryptoContext
from typing_extensions import deprecated


class PasswordEncrypt:

    pwd_context = CryptoContext(schemas=['bcrypt'], deprecated='auto')

    @classmethod
    async def get_password_hash(cls, password: str) -> str:
            return cls.pwd_context.hash(password)


    @classmethod
    async def verify_password(cls, plain_password: str, hashed_password: str) -> bool:
        return cls.pwd_context.verify(plain_password, hashed_password)