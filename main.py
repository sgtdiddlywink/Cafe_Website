# Import Modules
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

# Create app object from Flask Class
app = Flask(__name__)

# Connect to SQL Database. This can be customized and modified with a different Database if wanted
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"  # Configure the app object to link back to database
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # Turn modification tracking off on app object
db = SQLAlchemy(app)  # Database object utilizing SQLAlchemy and utilizing the app object as an input


# Create Cafe Class if input of the database object
class Cafe(db.Model):
    # Set columns of the SQL database
    id = db.Column(db.Integer, primary_key=True)  # ID column
    name = db.Column(db.String(250), unique=True, nullable=False)  # Name column
    map_url = db.Column(db.String(500), nullable=False)  # map_url Column
    img_url = db.Column(db.String(500), nullable=False)  # img_url Column
    location = db.Column(db.String(250), nullable=False)  # Location Column
    has_sockets = db.Column(db.String(250), nullable=False)  # Has sockets Column. 0 = False & 1 = True
    has_toilet = db.Column(db.String(250), nullable=False)  # Has toilets Column. 0 = False & 1 = True
    has_wifi = db.Column(db.String(250), nullable=False)  # Has wifi Column. 0 = False & 1 = True
    can_take_calls = db.Column(db.String(250), nullable=False)  # Can take calls Column. 0 = False & 1 = True
    seats = db.Column(db.String(250), nullable=False)  # How many seats Column
    coffee_price = db.Column(db.String(250), nullable=False)  # Price of coffee column

    # Method to return a dictionary of the database
    def to_dict(self):
        # Use dictionary comprehension to return a dictionary of all items in the database
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


# Set home page routing
@app.route("/")
def home():
    cafes = db.session.query(Cafe).all()  # Pull all cafe data into an object
    return render_template("index.html", all_cafes=cafes)  # Returns index.html page from templates folder


# Page to display json of the database
@app.route("/all")
def all_cafes():
    cafes = db.session.query(Cafe).all()  # Pull all cafe data into an object
    return jsonify(cafe=[cafe.to_dict() for cafe in cafes])  # return a json list of all the cafes in the database


# Initiate the script and start a development server
if __name__ == "__main__":
    app.run(debug=True)
