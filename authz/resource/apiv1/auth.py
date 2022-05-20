from flask_restful import Resource
from authz.controller.apiv1 import AuthController

class AuthResource(Resource):
    def get(self):
        return AuthController.verify_jwt_token()
    def post(self):
        return AuthController.create_jwt_token()
