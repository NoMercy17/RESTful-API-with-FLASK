from flask import jsonify, request
from app import app, db, auth  # Add auth to imports
from app.models.user import User
from app.schemas.user_schema import users_schema
from werkzeug.security import generate_password_hash, check_password_hash  # Add check_password_hash
from flask_jwt_extended import create_access_token

@app.route('/users', methods=['GET'])
def users():
    user_list = User.query.all()
    result = users_schema.dump(user_list)
    return jsonify(result)

@app.route('/register', methods= ['POST'])
def register():
    data = request.get_json()
    hash_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(first_name=data['first_name'],
                    last_name=data['last_name'],
                    email_address=data['email_address'],
                    password=hash_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify(message="Registered successfully!"), 201


@app.post('/login')
def login():
    data = request.get_json()
    if not data:
        return {"message": "Invalid or missing JSON data"}, 400

    email = data.get('email_address')
    password = data.get('password')

    #print(f"Login attempt: {email} / {password}")

    user = User.query.filter_by(email_address=email).first()

    if not user:
        print("User not found.")
        return {"message": "Bad user name"}, 401

    #print(f"User found: {user.email_address}")
    #print(f"Stored hash: {user.password}")
    
    if not check_password_hash(user.password, password):
        print("Password incorrect.")
        return {"message": "Bad password"}, 401

    print("Login successful.")
    access_token = create_access_token(identity=email)
    return {"message": "Successful login", "access_token": access_token}


print("LOADING AUTH FUNCTION...")
@auth.verify_password
def verify_password(email, password):
    print("=== AUTH FUNCTION CALLED ===")
    #print(f"Email: '{email}'")
    #print(f"Password: '{password}'")
    
    user = User.query.filter_by(email_address=email).first()
    print(f"User found: {user is not None}")
    
    if user:
        #print(f"Stored password hash: {user.password[:20]}...")
        password_valid = check_password_hash(user.password, password)
        #print(f"Password valid: {password_valid}")
        
        if password_valid:
            print("AUTH SUCCESS!")
            return True
        else:
            print("AUTH FAILED - wrong password")
            return False
    else:
        print("AUTH FAILED - user not found")
        return False

print("AUTH FUNCTION REGISTERED!")