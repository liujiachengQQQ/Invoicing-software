from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy()
migrate = Migrate(db=db)

def ext_init(app):
    bootstrap.init_app(app) #bootstrap
    db.init_app(app) #模型的对象
    migrate.init_app(app) #模型迁移对象