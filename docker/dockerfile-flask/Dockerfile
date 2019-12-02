FROM python:3.8-buster

ENV APP /app

RUN mkdir $APP
WORKDIR $APP

COPY requirements.txt /tmp

RUN apt-get update && apt-get -y install netcat \
    && pip install --upgrade pip && pip install -r /tmp/requirements.txt