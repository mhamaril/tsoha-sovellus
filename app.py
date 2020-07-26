from flask import Flask
from flask import redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)

@app.route("/")
def index():
    db.session.execute("INSERT INTO visitors (time) VALUES (NOW())")
    db.session.commit()
    result = db.session.execute("SELECT COUNT(*) FROM visitors")
    counter = result.fetchone()[0]
    return render_template("index.html", counter=counter) 

@app.route("/submitlabs")
def submit():
    return render_template("submitlabs.html")

@app.route("/result", methods=["POST"])
def result():
    sex = request.form["sex"]
    age = request.form["age"]
    diet = request.form["diet"]
    hours = request.form["hours"]
    units = request.form["units"]
    total = request.form["total"]
    ldl = request.form["ldl"]
    hdl = request.form["hdl"]
    trigly = request.form["trigly"]
    return render_template("result.html", sex = sex, age = age, diet = diet, hours = hours, units = units, total = total, ldl = ldl, Hdl = hdl, trigly = trigly)
