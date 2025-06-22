from flask import Flask
from flask_babel import Babel

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(app)

from app import routes
