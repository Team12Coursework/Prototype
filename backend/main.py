from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app import init_db
from app.api import router

app = FastAPI(
    title='CharacterConnect',
    docs_url='/',
    version='0.0.1',
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(
    router.router,
    prefix='/api'
)

init_db.init()