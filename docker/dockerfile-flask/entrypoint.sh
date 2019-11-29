#!/bin/sh

export FLASK_ENV=development
export FLASK_APP=app

#flask db migrate
#flask db upgrade

#gunicorn -b :5000 app:app

flask run --host=0.0.0.0