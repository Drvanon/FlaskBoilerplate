"""
Implementation of the endpoints of the application.
"""

import os
import logging
from flask import request, abort
from flask_restful import Resource
from marshmallow import ValidationError
from schemas import RegisterSchema
from controllers import register_user


def schema_loader(schema, inp):
    """
    Helper function that aborts a request if the schema of the resource fails,
    returning the first reason why it failed.
    """
    try:
        data = schema.load(inp)
    except ValidationError as err:
        field = list(err.messages.keys())[0]
        abort(400, f"{field}: {err.messages[field][0]}")
    else:
        return data


class RegisterResource(Resource):
    """
    Resource opening up an endpoint for a client to register via the API.
    """
    schema = RegisterSchema()

    def post(self):
        """
        Register a user with an email and a name.
        """
        logging.debug("Receiving post in thread with pid: %d", os.getpid())
        data = schema_loader(self.schema, request.get_json())
        return {"id": register_user(data["name"], data["email"])}
