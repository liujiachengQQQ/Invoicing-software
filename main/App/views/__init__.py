from .index import main

blueprintConfig = [
    (main, ''),
]


#注册蓝本
def register_blueprint(app):
    for blueprint,prefix in blueprintConfig:
        app.register_blueprint(blueprint,url_prefix=prefix)