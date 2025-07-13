from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask import Flask

from dotenv import load_dotenv
import os


load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

with app.app_context():
    db.create_all()
