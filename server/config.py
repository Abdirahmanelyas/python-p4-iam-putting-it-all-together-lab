from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = b'your-secret-key-here'  # replace with your secret key

db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)
bcrypt = Bcrypt(app)