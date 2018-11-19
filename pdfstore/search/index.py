from flask import Blueprint


mod4 = Blueprint('search',__name__)


@mod4.route('/')
def index():
    return 'hi from search.index.py'
