import os
from pathlib import Path
from dotenv import load_dotenv


# Database configuration
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
database = os.getenv('DB')


class Config(object):
    ENV_FILE_PATH = Path('.') / '.env'
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv('SECRET_KEY')
    # jwt configuration
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = 600  # jwt token expires after 10 minutes

    # Args parser configuration
    PROPAGATE_EXCEPTIONS = True

    # database configuration
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'

    # Media files location
    FILES_STORAGE_PATH = os.getenv('FILES_STORAGE_PATH')

    # MAX FILESIZE
    MAX_CONTENT_LENGTH = 25 * 1024 * 1024  # max content length in bytes

    def __init__(self):
        load_dotenv(dotenv_path=self.ENV_FILE_PATH)


class ProductionConfig(Config):
    DEBUG = False
    ENV_FILE_PATH = Path('.') / '.env'


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
