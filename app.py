from flask import (
    Flask,
    flash, 
    render_template, 
    redirect,
    request,
    url_for,
    make_response,
    jsonify
)
from flask_restful import Resource, Api, reqparse
from flask_httpauth import HTTPBasicAuth
from functools import wraps
from flask_sqlalchemy import SQLAlchemy
from users import USERS
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import os

app = Flask(__name__)
api = Api(app, prefix="/api/v1")
auth = HTTPBasicAuth()

app.config["SECRET_KEY"] = datetime.utcnow().strftime("%Y-%m-%d") + "This is a secret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.getcwd() + '/user.db'


db = SQLAlchemy(app)



class UserDB(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(80), unique=True)
    admin = db.Column(db.Boolean)
    
db.create_all()

class User(Resource):
    def post(self):
        user_data = request.get_json()
        print("User Data",user_data)

        password_hashed = generate_password_hash(user_data["password"], method='sha256')
        new_user = UserDB(public_id=str(uuid.uuid4()),
                            username=user_data["username"],
                            password=password_hashed,
                            email=user_data["email"],
                            admin=False)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message' : f'New user is created. public_id:{new_user.public_id}'})
    
    def get(self):
        users = UserDB.query.all()
        output = []
        for user in users:
            user_data = {}
            user_data['public_id'] = user.public_id
            user_data['username'] = user.username
            user_data['admin'] = user.admin
            output.append(user_data)

        return jsonify({'users' : output})


    def get_one_user(self):
        parser = reqparse.RequestParser()
        parser.add_argument('public_id', help='PublicID')
        args = parser.parse_args() 
        public_id = args.public_id

        user = User.query.filter_by(public_id=public_id).first()

        if not user:
            return jsonify({'message' : 'No user found!'})

        user_data = {}
        user_data['public_id'] = user.public_id
        user_data['name'] = user.name
        user_data['admin'] = user.admin

        return jsonify({'user' : user_data})





@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return USERS.get(username) == password


class Test(Resource):
    @auth.login_required
    def get(self):
        # http://127.0.0.1:64953/api/v1/test?name=Erdem&surname=Sirel
        name = request.args.get("name")
        surname = request.args.get("surname")
        data = request.get_json()
        return{'data': "Test",
                'name':name,
                'surname': surname,
                'data': data}


# Register Resources
api.add_resource(Test, "/test")
api.add_resource(User, "/user" )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)