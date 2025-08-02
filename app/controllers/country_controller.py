from flask import jsonify, request
from app import app, db, auth
from app.models.country import Country
from app.schemas.country_schema import countries_schema, country_schema
from flask_jwt_extended import jwt_required

@app.route('/countries', methods=['GET'])
@auth.login_required() # it requires the login 
@jwt_required()

def countries():
    country_list = Country.query.all()
    result = countries_schema.dump(country_list)
    return jsonify(result)

@app.route('/country_details/<int:country_id>', methods=['GET'])
@jwt_required()
def country_details(country_id: int):
    country_variable = Country.query.filter_by(country_id=country_id).first()
    if country_variable:
        result = country_schema.dump(country_variable)
        return jsonify(result)
    else:
        return jsonify("That country does not exist!"), 404

@app.route('/add_country', methods=["POST"])
def add_country():
    country_name = request.form['country_name']
    check_country = Country.query.filter_by(country_name=country_name).first()
    if check_country:
        return jsonify("The country already exists in DB")
    
    capital = request.form['capital']
    area = request.form['area']
    population = request.form['population']
    new_country = Country(country_name=country_name, capital=capital, area=area, population=population)
    db.session.add(new_country)
    db.session.commit()
    return jsonify(message="You added a new country"), 201

@app.route('/add_country1', methods=['POST'])
def add_country1():
    data = request.get_json()
    if not data:
        return jsonify("Invalid/missing JSON data")
    
    country_name = data.get('country_name')
    check_country = Country.query.filter_by(country_name=country_name).first()
    if check_country:
        return jsonify("The country already exists in DB")
    
    capital = data.get('capital')
    area = data.get('area')
    population = data.get('population')  # Fixed: was missing
    new_country = Country(country_name=country_name, capital=capital, area=area, population=population)
    
    db.session.add(new_country)
    db.session.commit()
    return jsonify(message="You added a new country"), 201

@app.route('/countries/<int:country_id>', methods=["PATCH"])
def update_country(country_id):
    data = request.get_json()
    country = Country.query.filter_by(country_id=country_id).first()
    if not country:
        return jsonify(message="Country not found!"), 404
    
    if 'country_name' in data:
        country.country_name = data['country_name']
    if 'capital' in data:
        country.capital = data['capital']
    if 'area' in data:
        country.area = data['area']
    if 'population' in data:
        country.population = data['population']
    
    db.session.commit()
    return jsonify({"message": "Country updated successfully!", "country_id": country_id})

@app.route('/countries/<int:country_id>', methods=['DELETE'])
def remove_country(country_id: int):
    country = Country.query.filter_by(country_id=country_id).first()
    if not country:
        return jsonify(message="Country not found!"), 404
    
    db.session.delete(country)
    db.session.commit()
    return jsonify(message=f"You deleted the country with the id: {country_id}"), 202