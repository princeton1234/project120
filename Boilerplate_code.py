#Importing flask module in the project
from flask import Flask

#Create an object of the Flask class
app = Flask(__name__)

#The route() function of the Flask class 
@app.route("/")
def home():
    name = "Princeton"
    age = "13"
@app.route("/")
def father():
    name = "father"
    age = "47"
@app.route("/")
def mother():
    name = "mother"
    age = "42"
@app.route("/")
def friend():
    name = "John"
    age = "12"       

#‘/’ URL is bound with first_flask function.
def first_flask():

    return "This is my first flask program"

#run the application on local server
app.run()
