"""
Entrypoint of the application, tying all pieces of the API together and
preparing it to be accessed by a HTTP server like gunicorn, uwsgi etc.

Run with:

```bash
$ pipenv run flask run
```
"""
import logging
import os
from flask import Flask
from api import create_api
from database import initialize_database


def load_config(app):
    """
    Stub for actual configuration loading function.
    """
    app.config["DB_URL"] = "sqlite:///db.sqlite"


def create_app():
    """
    WSGI entry point to the api.
    """
    app = Flask(__name__)

    load_config(app)
    if app.config["DEBUG"]:
        logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
        logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
    else:
        logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

    logging.debug("Creating application in thread with pid: %d", os.getpid())

    @app.before_first_request
    def load_database():
        initialize_database(app.config["DB_URL"])

    create_api(app)
    return app
