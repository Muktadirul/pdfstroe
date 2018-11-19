from flask import Blueprint


mod1 = Blueprint('api',__name__)

'''
user api route
'''
@mod1.route('/create_user')
def user_create():
    return 'hi 1 create_user from api.index.py'

@mod1.route('/register')
def register():
    return 'hi 1 register from api.index.py'

@mod1.route('/login')
def login():
    return 'hi 1 login from api.index.py'
'''
Authorization api route
'''

'''
search api route
'''

'''
solve api route
'''

'''
request api route
'''
