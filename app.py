from flask import Flask, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Person

app = Flask(__name__)

app.config['SQLALCHEMY_ECHO']= True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///test_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'Germanshepherdsarethebest'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

