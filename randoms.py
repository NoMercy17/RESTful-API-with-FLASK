
# # Routes
# @app.route('/')  # defines the root for endpoint
# def hello_world():
#     return 'Hello, World!'

# @app.route('/simple')
# def simple():
#     return jsonify(text='Hello, Simple World!',
#                    message='The api is working')

# @app.route('/not_found')
# def not_found():
#     return jsonify(error='This route was not found!'), 404

# @app.route('/parameters')  # we modify this from .com/?name=Antonio&age=20 -> .com/Antonio20
# def parameters():
#     name = request.args.get('name')
#     age_str = request.args.get('age')
    
#     if not name or not age_str:
#         return jsonify(error='Missing name or age parameter'), 400
    
#     try:
#         age = int(age_str)
#     except ValueError:
#         return jsonify(error='Age must be a number'), 400
    
#     if age > 18:
#         return jsonify(message=f"Welcome {name}!!")
#     else:
#         return jsonify(message=f"SRY {name}, not old enough!!")

# @app.route('/api_variables/<string:name>/<int:age>')
# def api_variables(name: str, age: int):
#     if age > 18:
#         return jsonify(message=f"Welcome {name}!!")
#     else:
#         return jsonify(message=f"SRY {name}, not old enough!!")


