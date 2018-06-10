from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
#from sqlalchemy_utils import database_exists, create_database
import os
import csv
from sqlalchemy.orm import scoped_session, sessionmaker
#import requests
#from models import *

app = Flask(__name__)
#db_conn = 'postgresql://postgres:postgres@localhost/db'
#app.config['SQLALCHEMY_DATABASE_URI'] = db_conn
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#db = SQLAlchemy(app)
'''
class Light(db.Model):
    __tablename__ = "lights"
    id = db.Column(db.Integer,primary_key =True)
    status = db.Column(db.Float,nullable = False)
    pop = db.Column(db.Float,nullable = False)

    def __init__ (self,value,pop):
        self.value = value
        self.pop = pop

    def __rep__(self):
        return '<status %r>' %self.status
'''
#f = open("data/sloc.csv")
#reader = csv.reader(f)


@app.route("/<string:name>")
def index(name):
    name = name.capitalize()
    #for id,status,pop in reader:
        #db.create_all()
    #return render_template("Index.html")
    return f"{name}, is a homo"

#@app.route("/Dashboard", methods=["POST"])
#def dash(light):
#    return f"Hello!"
