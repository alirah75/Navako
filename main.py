from fastapi import FastAPI, status
from apis.base import api_router


def include_router(app):
    app.include_router(api_router)


def start_app():
    app = FastAPI(title='Navako-tests', version='1.0.0')
    include_router(app)
    return app


app = start_app()


@app.get('/', status_code=status.HTTP_200_OK)
def home():
    return {"msg": "Welcome NLP model performs emotion recognition"}
