#!/bin/sh

export FLASK_ENV=development
export FLASK_APP=models

[ -d "migrations" ] && echo "Directory migrations exists." && flask db upgrade
[ ! -d "migrations" ] && echo "Directory migrations DOES NOT exists." &&  flask db init
flask db migrate


#gunicorn -b :5000 app:app

export FLASK_APP=app
flask run --host=0.0.0.0