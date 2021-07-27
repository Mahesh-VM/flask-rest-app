"""
UserModel containing the username as first_name, last_name, and
password with autoincrementing column user_id.
"""
from typing import Any

from flask_rest_app.db import db


class UserModel(db.Model):
    """Declared the table name and the schema to be used."""

    __tablename__ = "users"
    __table_args__ = {"schema": "sch"}

    id = db.Column("user_id", db.Integer, primary_key=True, autoincrement=True)
    username = db.Column("first_name", db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=True)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, _id, username, password):
        self.id = _id
        self.first_name = username
        self.password = password

    @classmethod
    def find_by_username(cls, username) -> Any:
        """Filter the table for a given username/first_name."""
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, users_id) -> Any:
        """Filter the table for a given user id."""
        return cls.query.filter_by(id=users_id).first()
