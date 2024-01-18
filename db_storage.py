#!/usr/bin/python3
"""importing the modules"""

import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import City, State, Review, Amenity, Place, User

Base = declarative_base()

class DBStorage:
    """class defination"""

    __engine = None
    __session = None

    def __init__(self):
        """public instance method"""
        usr = os.environ.get('HBNB_MYSQL_USER')
        pwd = os.environ.get('HBNB_MYSQL_PWD')
        hst = os.environ.get('HBNB_MYSQL_HOST', 'localhost')
        dtb = os.environ.get('HBNB_MYSQL_DB')
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(usr, pwd, hst, dtb), pool_pre_ping=True)

        if os.environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query current database and return a dictionary"""
        dictionary = {}
        if cls:
            objects = self.self__session.query(cls).all()
        else:
            objects = []
            for cls in [User, State, City, Amenity, Place, Review]:
                objects.extend(self.__session.query(cls).all())
        for obj in objects:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            dictionary[key] = obj
        return dictionary
    
    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        create all tables in the database
        """
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))
        self.__session = Session()

