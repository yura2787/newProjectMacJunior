from fastapi import FastAPI

from applications.users.router import user_router


def get_application() -> FastAPI:
    app = FastAPI(root_path="/api", root_path_in_servers=True)
    app.include_router(user_router, prefix="/users", tags=["Users"])

    return app
