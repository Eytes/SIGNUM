# Define a base stage that uses the official python runtime base image
FROM python:3.11-slim AS base

# Add curl for healthcheck
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*

# Set the application directory
WORKDIR /code

# Install our dependences
COPY pyproject.toml ./pyproject.toml
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    /root/.local/bin/poetry install --without test

FROM base
MAINTAINER Eytes <yura.shamanov2000@bk.ru>

COPY . .

ENTRYPOINT [ \
    "/root/.local/bin/poetry", "run", "uvicorn", "main:app", \
    "--proxy-headers", \
    "--host", "0.0.0.0", \
    "--port", "80" \
    ]