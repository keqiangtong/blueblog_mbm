
import os



class BaseConfig(object):
    SECRET_KEY=os.getenv('SECRET_KEY','as;lkdjdasdcjsa')
    SQLALCHEMY_DATABASE_URI='mysql://root:root@127.0.0.1:3306/blueblog_mbm'
    SQLALCHEMY_TRACK_MODIFICATIONS= True

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    pass


config_map ={
    'Development':DevelopmentConfig,
    'Production':ProductionConfig
}