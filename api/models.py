from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

# -------------------------------------------------------------------------- #
# Config & Flask-Migrate.
# -------------------------------------------------------------------------- #

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# -------------------------------------------------------------------------- #
# Models.
# -------------------------------------------------------------------------- #

class User(db.Model):
    """User Entity"""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)

    def create(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }


class Stock(db.Model):
    """Stock entity"""

    ticker = db.Column(db.String, primary_key=True)
    country = db.Column(db.String)
    broker = db.Column(db.String)
    date = db.Column(db.Date)
    price = db.Column(db.String)
    tax = db.Column(db.Float)

    def create(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @property
    def serialize(self):
        return {
            'ticker': self.ticker,
            'broker': self.broker,
            'date': self.date,
            'price': self.price,
            'tax': self.tax
        }
