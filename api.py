from flask_restful import Api
from resources import RegisterResource

def create_api(app):
    api = Api(app)
    api.add_resource(RegisterResource, "/register")
