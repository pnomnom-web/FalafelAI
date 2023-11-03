from database import db

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key = True)
    user = db.Column(db.String(30),unique=True, nullable=False)
    auth = db.Column(db.String,unique=True, nullable=False)