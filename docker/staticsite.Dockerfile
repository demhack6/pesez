FROM python:3.10-slim-bullseye AS builder
WORKDIR /build
# TODO USER builder
RUN python3 -m pip install poetry==1.4.1
COPY . /build
RUN poetry install
RUN poetry run python manage.py collectstatic --noinput

FROM nginx:1.22.1
COPY nginx/proxy.conf /etc/nginx/conf.d/
COPY --from=builder /build/dst /var/www/data/static
