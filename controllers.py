"""
Collection of all business logic the application must be able to
perform.
"""
from contextlib import contextmanager
from sqlalchemy.exc import IntegrityError
from database import Session
from models import User


@contextmanager
def session_scope():
    """
    Context for dealing with sessions. This allows the developer not to have to
    worry perse about closing and creating the session.
    """
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def name_registered(name):
    """
    Confirm or deny the uniqueness of the given user in the database.
    """
    with session_scope() as session:
        if session.query(User).filter(User.name == name).one_or_none():
            return True
        return False


def email_registered(email):
    """
    Confirm or deny the uniqueness of the given email in the database.
    """
    with session_scope() as session:
        if session.query(User).filter(User.email == email).one_or_none():
            return True
        return False


def register_user(name, email):
    """
    Register a user in the database by a name and email.
    """
    with session_scope() as session:
        new_user = User(name, email)
        session.add(new_user)
        try:
            session.commit()
        except IntegrityError:
            session.rollback()
            raise
        else:
            return new_user.id
  