import os
project_dir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SSL_DISABLE = False

    @staticmethod
    def init_app(app):
        pass


class Dev(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'driver://user:pass@hostname/dbname'
    SQLALCHEMY_ECHO = True


class Test(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(project_dir, 'test.sqlite')


config = {
    'test': Test,
    'dev': Dev
}
