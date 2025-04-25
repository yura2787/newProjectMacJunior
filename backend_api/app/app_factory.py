from fastapi import FastAPI

def get_application():
    app = FastAPI(root_path="/api", root_path_in_servers=True)
    return app