from flask import Blueprint


mod3 = Blueprint('resolve',__name__)


@mod3.route('/')
def index():
    return 'hi from resolve.index.py'
