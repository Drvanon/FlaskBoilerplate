"""
Collection of all tables in the database with appropriate setters.
"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from database import Base

class User(Base):
    """
    Classical user model with id, name and email properties.
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)
    created = Column(DateTime())
    destroyed = Column(DateTime())

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email
        self.created = datetime.now()

    def destroy(self):
        """
        Destroy the user from the database.

        This is an example of a setter function, which should be created in the
        models.py file. It is not implemented very well.
        """
        self.destroyed = datetime.now()

    def __repr__(self):
        return '<User %r>' % (self.name)
