from flask import Blueprint, request, abort
from flask_restful import Api, Resource
from string import ascii_lowercase, digits
from schema import Schema, And, SchemaError
from app.controllers.user import create_user, update_best_point
import re

bp = Blueprint('user_api', __name__)
api = Api(bp)

# Format olusturma, sadece belirli bir formatı kabul eder
EMAIL_PATTERN = re.compile('[{}{}.]+@[{}]+.[{}]'.format(
    ascii_lowercase, digits, ascii_lowercase, ascii_lowercase))

CREATE_USER_SCHEMA = Schema({
    'email': And(str, lambda s: 0 < len(s) <= 60, EMAIL_PATTERN.match)
})


class User(Resource):

    def post(self):
        try:
            data = CREATE_USER_SCHEMA.validate(request.json)
        except SchemaError:
            print("Gecersiz Veri seti schema Error")
            abort(400)

        data = create_user(**data)
        if data:
            return {'status': 'OK',
                    'data': data}
        print('Data bulunamadi')
        abort(403)

    def put(self):
        email = request.json.get("email")
        point = request.json.get("point")

        if email:
            data = update_best_point(email, point)
            if data:
                return {'status': 'OK',
                        'best_point': data['best_point']}
            print('Data Bulunamadi')
            abort(403)

api.add_resource(User, '/api/user')
