import os
import config
from flask import Flask, request, render_template
from database import db
from twitch import twitch_blueprint

config.load_dotenv()
app = Flask(__name__)
app.register_blueprint(twitch_blueprint)

db_name = os.environ.get("DATABASE")
# Configuring SQLite Database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name

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

if __name__ == "__main__":
    from models import User
    create_db()
    app.run(debug=True, host='0.0.0.0', use_reloader=True)
