from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from time import sleep

from characterconnect import init_db
from characterconnect.api import router

"""
main program entrypoint.
This script may be invoked with uvicorn
using "python3 -m uvicorn main:app --reload"
"""

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

# there must be a better way of doing this :D. Just wait for
# 5 seconds before starting the database to ensure PostgreSQL
# can startup properly in the other Docker container.
sleep(2)
init_db.init()
