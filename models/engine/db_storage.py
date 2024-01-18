#!/usr/bin/python3
"""
Class that defines DBStorage class.
"""
from sqlalchemy import create_engine
from sqlalchemy.dialects.mysql import pymysql
from sqlalchemy.orm import sessionmaker, scoped_session, Session
from models.base_model import BaseModel, Base
from os import getenv


class DBStorage:
    __engine = None
    __session = None

    # class constructor that initializes the db variables
    def __init__(self):
        # Create the DB engine
        username = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db_name = getenv('HBNB_MYSQL_DB')
        db_url = 'mysql+mysqldb://{}:{}@{}/{}?charset=utf8'.format(username,
                                                           password,
                                                           host,
                                                           db_name)
        self.__engine = create_engine(db_url, pool_pre_ping=True)

        # Drop all tables if in test environment
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

        # Create a session
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()

    def all(self, cls=None):
        """
        Query the current db session all objs depending on class name (cls).
        If cls is None, query all object types.
        Args:
            cls (class): The class to query.

        Returns:
            dict: Dictionary with format {<class_name>.<object_id>: object}.
        """
        dict_obj = {}
        if cls:
            result_query = self.__session.query(cls).all()
        else:
            # Needed class for the query. You add others as needed
            classes = [State, City]
            result_query = []
            for cls in classes:
                result_query.extend(self.__session.query(cls).all())

        for obj in result_query:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            dict_obj[key] = obj

        return dict_obj

    def new(self, obj):
        """
        Add an object to the current db session.
        Args:
            obj: Object to be added into the db.
        """
        self.__session.add(obj)
        self.__session.commit()

    def save(self):
        """
        Commit all changes of the current db session.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete obj from current db session if not None

        Args:
        obj: Object to be removed from db.
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Create all tables in the database and
        create the current database session from the engine.
        """
        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(bind=self.__engine,
                                      expire_on_commit=False)
