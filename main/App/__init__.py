from flask import Flask
from .settings import configDict
from .extensions import ext_init
from .views import register_blueprint

def create_app(configName):
    app = Flask(__name__)
    app.config.from_object(configDict[configName]) #配置文件的加载
    ext_init(app)
    register_blueprint(app)

    return app