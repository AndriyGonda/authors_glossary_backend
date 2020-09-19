from passlib.apps import custom_app_context as pwd_context
from sqlalchemy.ext.hybrid import hybrid_property

from . import db


class User(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String, unique=True)
    is_admin = db.Column(db.Boolean, default=False)
    password_hash = db.Column(db.String(128))

    def __init__(self, name=None, password=None, is_admin=False):
        if password is not None:
            self.password_hash = self.generate_hash(password)
        self.name = name
        self.is_admin = is_admin

    @staticmethod
    def generate_hash(password):
        return pwd_context.encrypt(password)

    @hybrid_property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, new_password):
        self.password_hash = self.generate_hash(new_password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)
