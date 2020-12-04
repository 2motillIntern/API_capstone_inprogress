from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_marshmallow import Marshmallow

from flask_login import LoginManager

app = Flask(__name__)
#app.config.from_object(Config)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:Mia$wet16@localhost/accnt_api_db"
db = SQLAlchemy(app)
migrate = Migrate(app,db)
ma = Marshmallow(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

from accnt_api import models,routes