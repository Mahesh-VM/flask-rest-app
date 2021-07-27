"""
ItemModel containing the columns from the tables and functions
to interact with the table in the database.
"""
from datetime import datetime
from typing import Any, Dict

from flask_rest_app.db import db


class ItemModel(db.Model):
    """Declared the schema and table name to be used."""

    __tablename__ = "items"
    __table_args__ = {"schema": "STORE"}

    id = db.Column(
        "item_id", db.Integer, primary_key=True, autoincrement=True, nullable=False
    )
    name = db.Column("item_name", db.String(200), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=True)
    unit = db.Column(db.Float(precision=2), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now())

    def __init__(self, _id=None, name=None, price=None, unit=None, created_at=None):
        self.id = _id
        self.name = name
        self.price = price
        self.unit = unit
        self.created_at = created_at

    def json_data(self) -> Dict[str, Dict[str, float]]:
        """Generate dictionary for the item objects"""
        data_dict = {
            "item": {
                "id": self.id,
                "item_name": self.name,
                "price": float(self.price),
                "unit": float(self.unit),
                "created_at": self.created_at,
            }
        }
        return data_dict

    @classmethod
    def select_item_by_name(cls, item_name) -> Any:
        """Filter item using the item name."""
        return cls.query.filter_by(name=item_name).first()

    def insert_item(self) -> str:
        """Insert record with the required values for the column into the table."""
        db.session.add(self)
        db.session.commit()
        return "Record created."

    def delete_item(self) -> str:
        """Delete record from the table for the matching item name."""
        db.session.delete(self)
        db.session.commit()
        return "Record deleted."
