from accnt_api import app, db, ma, login_manager

from datetime import datetime

import uuid
from flask_login import UserMixin

from werkzeug.security import generate_password_hash, check_password_hash

from sqlalchemy import Table, Column, String, Date, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import DATE, MONEY, VARCHAR

base = declarative_base()

class Transaction(base):
    __tablename__ = 'transactions'

    transaction_id = Column(VARCHAR, primary_key=True)
    name = Column(VARCHAR)
    amount = Column(MONEY)
    date = Column(DATE)

    def __init__(self, transaction_id, name, amount, date):
        self.transaction_id = transaction_id
        self.name = name
        self.amount = amount
        self.date = date 

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.String(150), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100))
    password = db.Column(db.String(100), nullable = False)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    token = db.Column(db.String(400), default = 'No Token Created')
    token_refreshed = db.Column(db.Boolean, default = False)
    date_refreshed = db.Column(db.DateTime)

    def __init__(self,name,email,password,id = id):
        self.id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.password = self.set_password(password)

    def set_password(self,password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def __repr__(self):
        return f"Welcome {self.name}, let's see what's in your wallet."


