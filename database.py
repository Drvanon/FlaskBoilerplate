import logging
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

Base = declarative_base()
Session = scoped_session(sessionmaker())

def initialize_database(url):
    logging.debug("Initializing database")
    engine = create_engine(url)
    Base.metadata.create_all(engine)
    Session.configure(bind=engine)