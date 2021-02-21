from flask import (
    Flask,
    flash, 
    render_template, 
    redirect,
    request,
    url_for,
)
app = Flask(__name__)
app.secret_key = "ssssh don't tell anyone"


@app.route("/", methods=["GET"])
def index():
    print("test")
    return{'data': "Test"}

@app.route("/test", methods=["GET"])
def add_compliment():
    print("test- Erdem")
    return {'data': "Erdem/Test"}

if __name__ == '__main__':
    app.run()