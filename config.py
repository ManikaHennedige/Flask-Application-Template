import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'thissecretkeyissosecretyouwontguessit'
    # config mongodb here too (if you need to)
    # MONGODB_SETTINGS = { 'db' : {{ name of database }} }