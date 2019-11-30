#!/bin/sh

export FLASK_ENV=development

export FLASK_APP=models

flask db init
flask db migrate
flask db upgrade

#gunicorn -b :5000 app:app

export FLASK_APP=app
flask run --host=0.0.0.0