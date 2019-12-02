#!/bin/sh

# Waiting until postgres is up
# while ! nc -z postgres 5432; do sleep 1; done;
sleep 5

# Flask-Migrate
export FLASK_ENV=development
export FLASK_APP=models


[ ! -d "migrations" ] && echo "Directory migrations DOES NOT exists." &&  flask db init
flask db migrate
[ -d "migrations" ] && echo "Directory migrations exists." && flask db upgrade


#gunicorn -b :5000 app:app

# App - API
export FLASK_APP=app
flask run --host=0.0.0.0