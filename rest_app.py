"""
Main file to start the flask restful app. Consumes the credentials from
the env files and run on by default port 6000 on localhost.
"""
from decouple import config
from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from flask_rest_app.resources import Item, Items, UserRegisters
from flask_rest_app.security import authenticate, identity

rest_app = Flask(__name__)
rest_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config(
    "SQLALCHEMY_TRACK_MODIFICATIONS"
)
rest_app.config["SQLALCHEMY_DATABASE_URI"] = config("SQLALCHEMY_DATABASE_URI")
rest_app.secret_key = config("SECRET_KEY")
api = Api(rest_app)
jwt = JWT(rest_app, authenticate, identity)


api.add_resource(Item, "/item/<string:name>")
api.add_resource(Items, "/items/")
api.add_resource(UserRegisters, "/register/")

if __name__ == "__main__":
    from flask_rest_app.db import db

    db.init_app(rest_app)
    rest_app.run(port=6000, debug=True)
