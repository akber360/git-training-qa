from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")
db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), default="Didnotenter")
    last_name = db.Column(db.String(30), unique=True)  



@app.route("/")
def home():
    return "<h1>This is a title</h1>"

@app.route("/postoption", methods=["GET", "POST"])
def posto():
    response = request.method
    return f"Method is {response}"

# Every single app will have the following 2 lines of code exactly
if __name__ == "__main__":
    app.run(debug=True, host ="0.0.0.0", port=5000)