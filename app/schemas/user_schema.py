from app import ma
from marshmallow import fields

class UserSchema(ma.Schema):
    id = fields.Int()
    first_name = fields.Str()
    last_name = fields.Str()
    email_address = fields.Str()
    password = fields.Str()

user_schema = UserSchema()
users_schema = UserSchema(many=True)