from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from dotenv import load_dotenv
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager

load_dotenv()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///country.db'
app.config['JWT_SECRET_KEY'] = 'Antonio'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db = SQLAlchemy(app)
ma = Marshmallow(app)
auth = HTTPBasicAuth()

jwt = JWTManager(app)


# Register CLI commands directly here to avoid circular imports
@app.cli.command('db_create')
def db_create():
    db.create_all()
    print("Database created!")

@app.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print("Database dropped!")

@app.cli.command('db_insert')
def db_insert():
    from app.models.country import Country
    from app.models.user import User
    
    usa = Country(country_name="USA", capital="Washington", area=9833517, population=331900000)
    germany = Country(country_name="Germany", capital="Berlin", area=357114, population=83240000)

    db.session.add(usa)
    db.session.add(germany)

    test_user = User(first_name="Antonio", last_name="Stiube",
                     email_address="test@gmail.com", password="134568a")
    db.session.add(test_user)

    db.session.commit()
    print("Database inserted!")

# Import controllers AFTER 
from app.controllers import country_controller, user_controller, basic_controller

