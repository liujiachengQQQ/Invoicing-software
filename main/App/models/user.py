from App.extensions import db

class User(db.Model):
    __tablename__ = 'user' #起表名
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(12),index=True)
