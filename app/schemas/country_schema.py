from app import ma
from marshmallow import fields

class CountrySchema(ma.Schema):
    country_id = fields.Int()
    country_name = fields.Str()
    capital = fields.Str()
    area = fields.Float()
    population = fields.Int()

country_schema = CountrySchema()
countries_schema = CountrySchema(many=True)