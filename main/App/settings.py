import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

#配置文件
class Config:
    SECRET_KEY = 'asfzkhvmzzl123q4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234@10.31.157.71:3306/invoicing_softwarer'
    DEBUG = True
    TESTING= False

#配置的字典
configDict = {
    'default':DevelopmentConfig,
}