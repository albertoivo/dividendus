#!/bin/sh

pip install --upgrade pip

pip install -r /tmp/requirements.txt

export FLASK_ENV=development
export FLASK_APP=app

cd /app

gunicorn -b :5000 app:app