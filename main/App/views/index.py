from flask import Blueprint
from App.models import User #导入User模型类

main = Blueprint('main',__name__)


@main.route('/')
@main.route('/index/')
def index():
    return 'hello world'





