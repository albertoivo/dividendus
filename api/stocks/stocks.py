import datetime

import matplotlib.pyplot as plt
import pandas_datareader.data as pdr
import utils
from flask import Blueprint, jsonify, abort
from pandas_datareader._utils import RemoteDataError

stocks = Blueprint('stocks', __name__, url_prefix='/stocks')

now = datetime.datetime.now().date()
today = str(now)
last_month = str(now.replace(month=now.month - 1))
last_year = str(now.replace(year=now.year - 1))


@stocks.route('/ticker/<string:ticker>')
@stocks.route('/ticker/<string:ticker>/<string:start>/<string:end>')
def stock(ticker, start=last_month, end=today):
    """
    :param ticker: The stock ticker
    :param start: The start period to get values. Format 'YYYY-MM-DD'. Default is last month.
    :param end: the end period to get values. Format  'YYYY-MM-DD'. Default is today.
    :return: A complete JSON with prices and volume.
    """
    df = pdr.get_data_yahoo(ticker, start, end)
    # orient='index' makes the index to be the date (daily)
    json = df.to_json(double_precision=2, date_format='iso', orient='index')

    return json


@stocks.route('/graph/<string:ticker>')
@stocks.route('/graph/<string:ticker>/<string:start>')
@stocks.route('/graph/<string:ticker>/<string:start>/<string:end>')
@stocks.route('/graph/<string:ticker>/<string:start>/<string:end>/<string:kind>')
@stocks.route('/graph/<string:ticker>/<string:start>/<string:end>/<string:kind>/<string:colunm>')
def graph(ticker, start=last_month, end=today, kind='line', colunm='Adj Close'):
    """
    :param ticker: the stock ticker
    :param start: Default = last month
    :param end: Default = today
    :param kind: Default = line
    :param colunm: Default = Adj Close
    :return: a base64 matplotlib graph
    """
    try:
        df = pdr.get_data_yahoo(ticker, start, end)
        df[colunm].plot(kind=kind)
        return utils.matplotlib_to_base64(plt)
    except RemoteDataError as r:
        abort(404, r)
