#!/usr/bin/python3
""" holds class State"""
from models.base_model import BaseModel
from models.city import City
from models.config import storage_t  # <- import from config
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel):
    """Representation of a State"""

    if storage_t == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    if storage_t != "db":
        @property
        def cities(self):
            """getter for list of city instances related to the state"""
            city_list = []
            from models import storage  # local import avoids circular import
            all_cities = storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city
