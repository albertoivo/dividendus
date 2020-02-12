import logging
from logging import Formatter, FileHandler
import utils
from flask import Flask, jsonify, abort
from stocks.stocks import stocks

APPLICATION_NAME = "app.py"
app = Flask(__name__)

# -------------------------------------------------------------------------- #
# Blueprints register.
# -------------------------------------------------------------------------- #

app.register_blueprint(stocks)


# -------------------------------------------------------------------------- #
# Routes.
# -------------------------------------------------------------------------- #

@app.route('/')
def home():
    """Home."""
    return jsonify('Home')


@app.route('/api/help')
def api_help_json():
    """Print available functions."""

    func_list = {}
    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static':
            func_list[rule.rule] = app.view_functions[rule.endpoint].__doc__
    return jsonify(func_list)


@app.route('/converter/<float:amount>')
@app.route('/converter/<float:amount>/<string:currency>/<string:new_currency>')
def currency_converter(amount, currency='BRL', new_currency='USD'):
    """Convert amount from a currency to another one.

    :param float amount: The amount of `currency` to convert.
    :param str currency: The currency to convert from. Default to BRL.
    :param str new_currency: The currency to convert to. Default to USD.

    :return: The value of `amount` in `new_currency`.
    :rtype: float
    """

    currency = currency.upper()
    new_currency = new_currency

    try:
        result = utils.currency_converter(amount, currency, new_currency)
        return jsonify({
            currency: amount,
            new_currency: result
        })
    except ValueError as e:
        abort(400, e)


# -------------------------------------------------------------------------- #
# Error handler.
# -------------------------------------------------------------------------- #

@app.errorhandler(Exception)
def bad_request(e):
    return jsonify({
        'code': str(e.code),
        'name': str(e.name),
        'description': str(e.description)
    }), e.code


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')


if __name__ == '__main__':
    app.run()
