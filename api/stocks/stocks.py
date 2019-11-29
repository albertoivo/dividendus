from flask import Blueprint, jsonify
import pandas_datareader.data as pdr
import datetime

stocks = Blueprint('stocks', __name__, url_prefix='/stocks')

now = str(datetime.datetime.now().date())


@stocks.route('/ticker/<string:ticker>')
@stocks.route('/ticker/<string:ticker>/<string:start>/<string:end>')
def stock(ticker, start=now, end=now):
    """
    :param ticker: The stock ticker
    :param start: The start period to get values. Format 'YYYY-MM-DD' .
    :param end: the end period to get values. Format  'YYYY-MM-DD'.
    :return: A complete JSON with prices and volume.
    """

    df = pdr.get_data_yahoo(ticker, start, end)

    # orient = 'index' -> makes the index to be the date (daily)
    json = df.to_json(double_precision=2, date_format='iso', orient='index')

    return json
