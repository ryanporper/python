from flask_app import app
from flask import render_template

from flask_app.model.model_dojo import Dojo

@app.route("/")
def index():
    # call the get all classmethod to get all dojos
    dojos = Dojo.get_all()
    print(dojos)
    return render_template("index.html", dojos = dojos)