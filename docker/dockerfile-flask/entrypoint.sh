#!/bin/sh

export FLASK_ENV=development
export FLASK_APP=models

cd /app || exit

flask db migrate
flask db upgrade

gunicorn -b :5000 app:app


