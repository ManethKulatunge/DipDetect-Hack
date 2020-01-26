from flask import Flask, render_template, request, session, current_app
import code_nlp as mf

app = Flask(__name__)

@app.route("/")
def index():
    return current_app.send_static_file("prototypeConUHacksV.html")

@app.route("/hello", methods=['POST'])
def hello():
    if request.method == 'POST':
        name = request.form["name"]
        pm = mf.process_message('I am sad and depressed')
        return mf.sc_tf_idf.classify(pm)     
    