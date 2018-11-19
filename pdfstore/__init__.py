from flask import Flask
app = Flask(__name__)

from pdfstore.api.index import mod1
from pdfstore.request.index import mod2
from pdfstore.resolve.index import mod3
from pdfstore.search.index import mod4
from pdfstore.user.index import mod5

app.register_blueprint(api.index.mod1, url_prefix='/api/v1')
app.register_blueprint(request.index.mod2, url_prefix='/post')
app.register_blueprint(resolve.index.mod3, url_prefix='/solve')
app.register_blueprint(search.index.mod4, url_prefix='/search')
app.register_blueprint(user.index.mod5, url_prefix='/user')
