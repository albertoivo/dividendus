FROM python:3.8-buster

ENV APP /app

RUN mkdir $APP
WORKDIR $APP
#EXPOSE 5000

COPY requirements.txt /tmp

RUN pip install --upgrade pip && pip install -r /tmp/requirements.txt