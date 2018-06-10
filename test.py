from flask import Flask, render_template, url_for, request
app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/userReg", methods=["GET","POST"])
def userReg():
    return render_template("userReg.html")

@app.route("/camReg", methods=["GET","POST"])
def camReg():
    return render_template("camReg.html")

@app.route("/map", methods=["GET","POST"])
def map():
    return render_template("map.html")

@app.route("/submit", methods=["GET","POST"])
def submit():
    return render_template("submit.html")

#<string:name>

#
