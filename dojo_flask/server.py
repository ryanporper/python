from flask import render_template
from flask_app import app
from flask_app.controllers import controller_dojos, controller_ninjas
from flask_app.model.model_dojo import Dojo
            

@app.route('/')
def hi():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template("dojo.html", dojos=dojos)

if __name__ == "__main__":
    app.run(debug=True)