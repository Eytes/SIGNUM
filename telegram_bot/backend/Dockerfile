FROM python:3.11
MAINTAINER Eytes <yura.shamanov2000@bk.ru>

WORKDIR /code

COPY . .

RUN apt update -y && apt upgrade -y

# install poetry and dependences
RUN python -m pip install --upgrade pip \
    && python3 -m pip install --user pipx \
    && python3 -m pipx ensurepath \
    && pipx install poetry \
    && poetry install

ENTRYPOINT ["poetry", "run", "uvicorn", "main:app"]