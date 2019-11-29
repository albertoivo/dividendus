import base64
from io import BytesIO

from currency_converter import CurrencyConverter
from flask import jsonify


def matplotlib_to_base64(plt):
    """
    Transform a Matplotlib graph to a base 64 url.

    :param plt: The matplotlib graph after plotting it.
    :return: the matplotlib graph in base64.
    """
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())
    result = 'data:image/png;base64,{}'.format(figdata_png.decode("utf-8"))

    return result


def currency_converter(amount, currency, new_currency):
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

    return result
