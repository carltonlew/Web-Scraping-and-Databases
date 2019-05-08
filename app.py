# Import libraries
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
# import mars_scrape

# Create an instance of Flask app
app = Flask(__name__)

# Use flask_pymongo to setup mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def home():
    marsdata = mongo.db.mars_data.find()

    return render_template("index.html", marsdata=marsdata)


