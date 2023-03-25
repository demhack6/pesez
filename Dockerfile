FROM python:3.10-slim-bullseye AS builder
WORKDIR /build
# TODO USER builder
RUN python3 -m pip install poetry==1.4.1
COPY ./poetry.lock ./pyproject.toml /build/
RUN poetry export -f requirements.txt --output requirements.txt
RUN python3 -m venv /build/.env
RUN /build/.env/bin/python -m pip install -r requirements.txt

FROM python:3.10-slim-bullseye
# TODO USER www
COPY . /app
WORKDIR /app
COPY --from=builder  /build/.env /app/.env
ENTRYPOINT /app/.env/bin/python manage.py runserver 0.0.0.0:8000
