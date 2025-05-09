from sqlalchemy.ext.asyncio import create_async_engine

from settings import settings

engine = create_async_engine(settings.DATABASE_URL_ASYNC, echo=True)
