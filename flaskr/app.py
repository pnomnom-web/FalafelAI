import os
import config
from flask import Flask, request, render_template
from database import db
from twitch import twitch_blueprint

config.load_dotenv()
app = Flask(__name__)

def create_test_app():
    app.config['TESTING'] = True
    app.register_blueprint(twitch_blueprint)
    # Configuring SQLite Database URI
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.environ.get("TEST_DATABASE")
    # Suppresses warning while tracking modifications
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # Initialising SQLAlchemy with Flask App
    db.init_app(app)

def create_prod_app():
    app.register_blueprint(twitch_blueprint)
    # Configuring SQLite Database URI
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.environ.get("DATABASE")
    # Suppresses warning while tracking modifications
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # Initialising SQLAlchemy with Flask App
    db.init_app(app)

#Creating Database with App Context
def create_db():
    with app.app_context():
        db.create_all()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/drop")
def drop_database():
    db.drop_all()
    return render_template("index.html")

if __name__ == "__main__":
    from models import User, Pet
    create_test_app()
    create_db()
    app.run(debug=os.environ.get("DEBUG"), host='0.0.0.0', use_reloader=os.environ.get("DEBUG"))
