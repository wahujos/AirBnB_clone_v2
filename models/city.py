#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    # Columns
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), FoerignKey('state.id'), nullable=False)
    state = relationship('State', back_populates='cities)
