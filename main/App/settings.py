import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

#配置文件
class Config:
    SECRET_KEY = 'asfzkhvmzzl123q4'

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING= False

#配置的字典
configDict = {
    'default':DevelopmentConfig,
}