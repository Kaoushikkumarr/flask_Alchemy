# Creating Database and updating configuration

import os

# ACCESS path for directory

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):  # Adding Config class by extending object
    DEBUG: bool = False
    TESTING: bool= False
    CSRF_ENABLED: bool = True
    SECRET_KEY: str = 'this-really-needs-to-be-changed'  # for security purpose
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']  # Adding SQLALCHEMY_DATABASE_URI


class ProductionConfig(Config):  # Adding class ProductionConfig()  # Baseclass: Config()
    DEBUG: bool = True


class StagingConfig(Config):  # Adding class StagingConfig()  # Baseclass: Config()
    DEVELOPMENT: bool = True
    DEBUG: bool = True


class TestingConfig(Config):  # Adding class # Adding class TestingConfig()  # Baseclass: Config()
    TESTING: bool = True