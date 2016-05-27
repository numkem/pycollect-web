from flask import Flask
from flask.ext.bower import Bower
from flask.ext.pymongo import PyMongo
from flask.ext.login import LoginManager
from flask.ext.bootstrap import Bootstrap
from flask.ext.debugtoolbar import DebugToolbarExtension
import logging

app = Flask('application')

app.config.from_pyfile('../etc/config.cfg')

if app.config['DEBUG']:
    toolbar = DebugToolbarExtension(app)

Bower(app)
Bootstrap(app)
mongo = PyMongo(app)

from filters import *
from application.views import *
