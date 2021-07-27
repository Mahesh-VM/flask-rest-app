"""
Contains the UserRegisters resource class to register a new user.
"""
from db_conn import ServerDb
from flask_restful import Resource, reqparse


class UserRegisters(Resource):
    """Parse the post data and validation checks on post data."""

    parser = reqparse.RequestParser()
    parser.add_argument(
        "first_name", type=str, required=True, help="Specify the first_name."
    )
    parser.add_argument(
        "last_name", type=str, required=True, help="Specify the last_name."
    )
    parser.add_argument("password", type=str, required=True, help="Password required.")

    def post(self):
        """Parsed post data is inserted into the UserModel."""
        data = UserRegisters.parser.parse_args()
        db_cursor = ServerDb()
        query = "insert into sch.users values (?, ?, ?)"
        db_cursor.query_maker(
            query=query,
            filter_tuple=(
                data["first_name"],
                data["last_name"],
                data["password"],
            ),
            query_type="insert",
        )
        db_cursor.db_close()

        return {"message": "User ccreated."}, 201
