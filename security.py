"""Provides method/function to be consumed in the JWT function to create access_token"""
from flask_rest_app.models import UserModel


def authenticate(username, pwd):
    """find the username from the UserModel and match the password."""
    user = UserModel.find_by_username(username)
    if user and pwd == user.password:
        return user


def identity(payload):
    """find the user by Id from the UserModel and return the user object."""
    user_id = payload["identity"]
    return UserModel.find_by_id(user_id)
