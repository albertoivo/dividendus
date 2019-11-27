from flask import Blueprint

stocks = Blueprint('stocks', __name__, template_folder='templates')


@stocks.route('/stocks')
def view():
    return "stock"

