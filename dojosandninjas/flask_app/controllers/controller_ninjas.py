from flask_app import app
from flask import render_template
from flask_app.model.model_ninja import Ninja

@app.route("/")
def index():
    # call the get all classmethod to get all ninjas
    ninjas = Ninja.get_all()
    print(ninjas)
    return render_template("index.html", ninjas = ninjas)