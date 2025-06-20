from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from poetry.utils.helpers import directory

from routers.main_page_router import router
from settings import settings


def get_application() -> FastAPI:
    app = FastAPI(debug=settings.DEBUG)
    app.include_router(router)

    app.mount('/static', StaticFiles(directory='static'), name='static')

    return app