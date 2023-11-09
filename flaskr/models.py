from database import db

class User(db.Model):
    __tablename__ = 'user'

    userid = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(30),unique=True, nullable=False)
    authid = db.Column(db.String,unique=True, nullable=False)

    def __init__(self, userid: int, username: str, authid: str):
        self.userid = userid
        self.username = username
        self.authid = authid
    
    @staticmethod
    def print_all_user(): 
        user_data = User.query.all() 
        return user_data

class Pet(db.Model):
    __tablename__ = 'pet'

    petid = db.Column(db.Integer, primary_key = True)
    userid = db.Column(db.Integer, db.ForeignKey('user.userid'))
    petName = db.Column(db.String(30), nullable=False)
    petVoice = db.Column(db.String(30), nullable=False)
    openpng = db.Column(db.String)
    closedpng = db.Column(db.String) # Both openPNG and closedPNG are both locations to where the PNG is stored.
    responses = db.Column(db.String) # Responses will hold a json literal for all the responses.


