from flask import jsonify, request
from app import app

# Basic routes
@app.route('/')  # defines the root for endpoint
def hello_world():
    return jsonify({
        "message": "Welcome to the Countries REST API!",
        "endpoints": {
            "countries": "/countries",
            "users": "/users",
            "country_details": "/country_details/<id>",
            "add_new user":"/register",
            "add_country": "/add_country (POST with form data)",
            "add_country1": "/add_country1 (POST with JSON)",
            "simple": "/simple",
            "parameters": "/parameters?name=YourName&age=25",
            "api_variables": "/api_variables/YourName/25"
        }
    })

@app.route('/simple')
def simple():
    return jsonify(text='Hello, Simple World!',
                   message='The API is working')

@app.route('/not_found')
def not_found():
    return jsonify(error='This route was not found!'), 404

@app.route('/parameters')  # Access with: /parameters?name=Antonio&age=20
def parameters():
    name = request.args.get('name')
    age_str = request.args.get('age')
    
    if not name or not age_str:
        return jsonify(error='Missing name or age parameter'), 400
    
    try:
        age = int(age_str)
    except ValueError:
        return jsonify(error='Age must be a number'), 400
    
    if age > 18:
        return jsonify(message=f"Welcome {name}!!")
    else:
        return jsonify(message=f"Sorry {name}, not old enough!!")

@app.route('/api_variables/<string:name>/<int:age>')
def api_variables(name: str, age: int):
    if age > 18:
        return jsonify(message=f"Welcome {name}!!")
    else:
        return jsonify(message=f"Sorry {name}, not old enough!!")