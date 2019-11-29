from flask import Blueprint, jsonify, json

stocks = Blueprint('stocks', __name__, url_prefix='/stocks')


@stocks.route('/all')
def view():
    acoes = {
                'Ticker': 'PETR3',
                'Valor': '25.50',
                'Data de Compra': '28/11/2019',
                'Corretora': 'Clear',
                'Taxa': '0.00'
            }, {
                'Ticker': 'ITUB4',
                'Valor': '36.00',
                'Data de Compra': '28/11/2019',
                'Corretora': 'Clear',
                'Taxa': '0.00'
            }
    return jsonify(acoes)
