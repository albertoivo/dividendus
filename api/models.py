from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects import postgresql

from config import Config

# -------------------------------------------------------------------------- #
# Config & Flask-Migrate.
# -------------------------------------------------------------------------- #


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# -------------------------------------------------------------------------- #
# Enum.
# -------------------------------------------------------------------------- #


operations = ('Buy', 'Sell')
operations_enum = postgresql.ENUM(*operations, name='operation')


# -------------------------------------------------------------------------- #
# Models.
# -------------------------------------------------------------------------- #


class User(db.Model):
    """User Entity"""

    email = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)

    stocks = db.relationship('Stock', lazy=True, cascade='delete')

    def create(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @property
    def serialize(self):
        return {
            'name': self.name,
            'email': self.email
        }


class Stock(db.Model):
    """Stock entity"""

    ticker = db.Column(db.String(10), primary_key=True)
    description = db.Column(db.String(250))

    user_email = db.Column(db.String, db.ForeignKey('user.email'))

    stock_details = db.relationship('StockDetail', lazy=True, cascade='delete')

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
            'description': self.description,
            'user_email': self.user_email
        }


class StockDetail(db.Model):
    """Stock Detail entity."""

    stock_ticker = db.Column(db.String, db.ForeignKey('stock.ticker'), primary_key=True)
    date = db.Column(db.Date, primary_key=True)
    operation = db.Column(operations_enum)
    price = db.Column(db.Float)
    tax = db.Column(db.Float)
    country = db.Column(db.String)

    @property
    def serialize(self):
        return {
            'stock_id': self.stock_id,
            'date': self.date,
            'operation': self.operation,
            'price': self.price,
            'tax': self.tax,
            'country': self.country
        }
