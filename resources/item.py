"""
Contains the Item and Items resoruce class which responds to the
incoming request for respective methods.
"""
from flask import jsonify, make_response
from flask_jwt import jwt_required
from flask_restful import Resource, reqparse

from flask_rest_app.models import ItemModel


class Item(Resource):
    """Contains http methods and response to fetch, update, create and delete items."""

    @jwt_required()
    def get(self, name: str):
        """Fetch an item using the item name from the ItemModel."""
        item = ItemModel.select_item_by_name(item_name=name)
        if item:
            return make_response(jsonify(item.json_data()), 200)
        return {"item": f"{name} not found"}, 404

    @jwt_required()
    def post(self, name: str):
        """Parse and validate the post data and create the item in ItemModel."""
        parser = reqparse.RequestParser()
        parser.add_argument("price", type=float, help="Price should be in float.")
        parser.add_argument("unit", type=float, help="Unit should be in float.")
        data = parser.parse_args()
        item_result = ItemModel.select_item_by_name(item_name=name)
        if item_result is not None:
            return {"message": f"An item with name " f"{name} already exists."}, 400
        item = ItemModel(name=name, price=data["price"], unit=data["unit"])
        qs = item.insert_item()
        return {"message": qs}, 201

    @jwt_required()
    def delete(self, name: str):
        """Delete an item from the ItemModel."""
        item_result = ItemModel.select_item_by_name(item_name=name)
        if item_result:
            qs = item_result.delete_item()
            return {"message": qs}, 200
        else:
            return {"message": "Item not available."}, 404

    @jwt_required()
    def put(self, name: str):
        """
        Parse the post data and update the item in ItemModel or
        create the item when no records are found in ItemModel.
        """
        parser = reqparse.RequestParser()
        parser.add_argument(
            "price", type=float, required=True, help="Price field is required."
        )
        parser.add_argument(
            "unit", type=int, required=True, help="Unit field is required."
        )
        data = parser.parse_args()
        item = ItemModel.select_item_by_name(item_name=name)

        if item is None:
            item = ItemModel(name=name, price=data["price"], unit=data["unit"])
            status_code = 201
            msg = "Record created."
        else:
            item.price = data["price"]
            item.unit = data["unit"]
            status_code = 200
            msg = "Record updated."
        item.insert_item()
        return {"message": msg}, status_code


class Items(Resource):
    """A generic resource class to fetch all the items in the ItemModel."""

    @jwt_required()
    def get(self):
        """Fetch the items fro the ItemModel."""
        return make_response(
            jsonify([item.json_data() for item in ItemModel.query.all()])
        )
