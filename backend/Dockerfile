FROM python:3.10

WORKDIR /app

# prevent Python from creating .pyc files, makes Dockerfile smaller
ENV PYTHONDONTWRITEBYTECODE TRUE
# prevent Python from buffering print statements, this is required to
# see logs in Docker
ENV PYTHONUNBUFFERED TRUE

ADD pyproject.toml .

# install poetry, don't use PIP to ensure that poetry deps are separated from python deps
# I believe this will end up creating a small image although I haven't tested it.
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
ENV PATH="${PATH}:/root/.poetry/bin"

# install dependencies with poetry
# disable creating venv as Docker is already a clean state
RUN poetry config virtualenvs.create false
RUN poetry install

COPY . .