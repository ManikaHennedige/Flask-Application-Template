from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
# from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_object(Config)

Bootstrap(app)

# db = MongoEngine()
# db.init_app(app)

from application import routes