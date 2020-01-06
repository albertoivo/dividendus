from flask import Blueprint, jsonify
import pandas as pd
import pandas_datareader.data as pdr
import datetime

from pandas_datareader._utils import RemoteDataError

import utils
import matplotlib.pyplot as plt

stocks = Blueprint('stocks', __name__, url_prefix='/stocks')

now = str(datetime.datetime.now().date())


@stocks.route('/ticker/<string:ticker>')
@stocks.route('/ticker/<string:ticker>/<string:start>/<string:end>')
def stock(ticker, start=now, end=now):
    """
    :param ticker: The stock ticker
    :param start: The start period to get values. Format 'YYYY-MM-DD'.
    :param end: the end period to get values. Format  'YYYY-MM-DD'.
    :return: A complete JSON with prices and volume.
    """
    df = pdr.get_data_yahoo(ticker, start, end)
    # orient='index' makes the index to be the date (daily)
    json = df.to_json(double_precision=2, date_format='iso', orient='index')

    return json


@stocks.route('/graph/<string:ticker>/<string:start>')
@stocks.route('/graph/<string:ticker>/<string:start>/<string:end>')
@stocks.route('/graph/<string:ticker>/<string:start>/<string:end>/<string:kind>')
@stocks.route('/graph/<string:ticker>/<string:start>/<string:end>/<string:kind>/<string:colunm>')
def graph(ticker, start, end=now, kind='line', colunm='Adj Close'):
    """

    :param ticker:
    :param start:
    :param end: Default=now
    :param kind: Default='line'
    :param colunm: Default='Adj Close'
    :return:
    """
    try:
    df = pdr.get_data_yahoo(ticker, start, end)
        df[colunm].plot(kind=kind)
        return utils.matplotlib_to_base64(plt)
    except RemoteDataError as r:
        return jsonify({'error': str(r)})
    except KeyError as r:
        return jsonify({'error': str(r)})
