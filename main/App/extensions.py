from flask_bootstrap import Bootstrap
from flask_migrate import Migrate

bootstrap = Bootstrap()
migrate = Migrate()

def ext_init(app):
    bootstrap.init_app(app) #bootstrap
    migrate.init_app(app) #模型迁移对象