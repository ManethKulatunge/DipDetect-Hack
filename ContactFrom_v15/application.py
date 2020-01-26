from flask import Flask, render_template, request, session, current_app

app = Flask(__name__)

@app.route("/")
def index():
    return current_app.send_static_file("prototypeConUHacksV.html")

@app.route("/hello", methods=['POST'])
def hello():
    if request.method == 'POST':
        name = request.form["name"]
        return name
    