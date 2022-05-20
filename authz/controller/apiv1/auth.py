from authz.util import jsonify
from jwt import encode, decode


class AuthController:

    def create_jwt_token():
        return jsonify(status=501, code=107)

    def verify_jwt_token():
        return jsonify(status=501, code=107)
