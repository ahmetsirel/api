from flask import (
    Flask,
    flash, 
    render_template, 
    redirect,
    request,
    url_for,
)
app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    print("test")
    name = request.args.get("name")
    surname = request.args.get("surname")
    return{'data': "Test",
            'name':name,
            'surname': surname}

@app.route("/test", methods=["GET"])
def add_compliment():
    print("test- Erdem")
    return {'data': "Erdem/Test"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)