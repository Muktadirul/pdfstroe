from flask import Blueprint


mod2 = Blueprint('request',__name__)


@mod2.route('/book/')
def index():
    return 'hi from request.index.py'
