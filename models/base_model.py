#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    # __tablename__ should be defined in each child class.
    __tablename__ = None

    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    # Save data into the db table
    def save(self):
        models.storage.new(self)
        models.storage.save()

    # Delete data from db table
    def delete(self):
        models.storage.delete(self)

    # Display data from table as a dict
    def to_dict(self):
        data = dict(self.__dict__)
        data.pop('_sa_instance_state', None)
        return data
