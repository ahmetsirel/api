from flask import (
    Flask,
    flash, 
    render_template, 
    redirect,
    request,
    url_for,
    make_response
)
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth
from functools import wraps
from users import USERS

app = Flask(__name__)
api = Api(app, prefix="/api/v1")
auth = HTTPBasicAuth()

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)