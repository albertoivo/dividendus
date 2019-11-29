from flask import Flask, jsonify, render_template, abort
from currency_converter import CurrencyConverter

from stocks.stocks import stocks

app = Flask(__name__)

# Blueprints register
app.register_blueprint(stocks)


@app.route('/')
def home():
    return render_template('pages/home.html')


@app.route('/api/help/json', methods=['GET'])
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

    # Pode instanciar o CurrencyConverter sem o parametro abaixo
    # É mais rápido porém desatualizado.
    c = CurrencyConverter('http://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip')
    result = c.convert(amount, currency, new_currency)

    return jsonify({
        currency: amount,
        new_currency: result
    })


@app.errorhandler(404)
def not_found(e):
    return jsonify({
        'code': '404',
        'description': str(e)
    }), 404


@app.errorhandler(403)
def forbidden(e):
    return jsonify({
        'code': '403',
        'description': str(e)
    }), 403


@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({
        'code': '500',
        'description': str(e)
    }), 500


if __name__ == '__main__':
    app.run(debug=True)
