from flask import Flask
from flask import request
from flask_debugtoolbar import DebugToolbarExtension
from flask import make_response
from flask import redirect
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("user.html")

@app.route("/test")
def test():
    return "test"

@app.route("/<name>")
def user(name):
    return '<h1>hello,%s!</h1>' % name

@app.route("/resp")
def resp():
    response = make_response('<h1>this document carries a cookies</h1>')
    response.set_cookie('answer','42')
    return response

@app.route("/baidu")
def tobaidu():
    return redirect("http://www.baidu.com")


if __name__ == '__main__':
    # the toolbar is only enabled in debug mode:
    app.debug = True

    # set a 'SECRET_KEY' to enable the Flask session cookies
    app.config['SECRET_KEY'] = '12345'
    toolbar = DebugToolbarExtension(app)
    app.run(host='localhost', port=5000)