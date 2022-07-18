from flask_app import app
from flask import redirect, render_template,request
from ..models.dojo import Dojo
from ..models.ninja import Ninja


@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    return render_template('dojos.html',all_dojos=Dojo.get_all())

@app.route('/create/dojo',methods=['POST'])
def create_dojo():
    data = {
        "name": request.form['name']
    }
    dojo_id = Dojo.save(data)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def show_dojo(id):
    data = {
        "id": id
    }
    return render_template('show_dojo.html',dojo=Dojo.select_one(data))