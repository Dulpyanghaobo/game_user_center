from flask import Flask, request, jsonify
from user_center.Models.models import db, User
from flask_login import login_user, LoginManager, login_required
from werkzeug.security import check_password_hash
from flask_migrate import Migrate


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/user_center'
app.secret_key = "demodemodmeodmeo"
db.init_app(app)
login_manager = LoginManager(app)
migrate = Migrate(app, db)


@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    user = User(username=username, email=email, password_hash=password)
    db.session.add(user)
    db.session.commit()
    return {'id': user.id}, 201

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    if user is None:
        return {"error": "not found"}, 404
    else:
        return {'username': user.username, 'email': user.email}

@app.route('/api/user/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({'error': 'Invalid credentials'}), 401

    login_user(user)
    return jsonify({'message': 'Logged in successfully'})
@app.route('/api/user/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'Registered successfully'})
@app.route('/api/user/update', methods=['POST'])
@login_required
def update_user():
    data = request.get_json()
    print(data)
    user_id = data.get('user_id')
    new_info = data.get('new_info') # new_info could be a dictionary containing the fields to be updated
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'message': 'User not found.'}), 404
    print(new_info)
    # update user information here
    # for example, if new_info is a dictionary like {'username': 'new_username'}
    for key, value in new_info.items():
        setattr(user, key, value)
    db.session.commit()
    return jsonify({'message': 'User information updated successfully.'}), 200
@app.route('/api/user/upgrade', methods=['POST'])
@login_required
def upgrade_user():
    data = request.get_json()
    user_id = data.get('user_id')
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'message': 'User not found.'}), 404
    # upgrade user level here
    # for example
    if user.user_level == None:
        user.user_level = 0
    user.user_level += 1
    db.session.commit()
    return jsonify({'message': 'User level upgraded successfully.'}), 200



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

if __name__ == '__main__':
    app.run()