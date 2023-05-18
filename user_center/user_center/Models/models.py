from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), unique=True, nullable=False)
    user_level = db.Column(db.Integer, unique=False, nullable= False)
    @property
    def active(self):
        return self.active
    def __repr__(self):
        return '<User %r>' % self.username
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)


