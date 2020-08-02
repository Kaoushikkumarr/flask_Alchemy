# creating the app.py file
# also importing models.py file
# importing SQLAlchemy and connect to the database:

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# object_creation
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Result  # from models.py file


@app.route('/')
def hello():
    """ can define logics here. """
    return "Hello, Kaoushik!"


@app.route('/<name>')
def hello_name(name):
    return "Hello, {}!".format(name)


if __name__ == '__main__':
    app.run()
