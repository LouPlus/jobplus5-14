class BaseConifg(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

class DevelopmentCofig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root@localhost:3306/simpledu?charset=utf8'

class ProductionConfig(BaseConfig):
    pass

class TestingConfig(BaseConfig):
    pass

configs = {
        'default': DevelopmentCofig,
        'development' : DevelopmentConfig,
        'production' : ProductionConfig,
        'testing' : TestingConfig
        }
