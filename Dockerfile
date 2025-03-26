FROM python:3.12-slim-bullseye

ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN pip install --upgrade pip poetry

RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction

COPY . .
