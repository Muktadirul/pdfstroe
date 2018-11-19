from flask import Blueprint


mod5 = Blueprint('user',__name__)


@mod5.route('/')
def index():
    return 'hi from user.index.py'
