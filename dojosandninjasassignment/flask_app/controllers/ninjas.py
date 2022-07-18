from flask_app import app
from flask import redirect, render_template,request
from ..models.ninja import Ninja

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')

@app.route('/create/ninja',methods=['POST'])
def create_ninja():
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "age": request.form['age'],
        "dojo_id": request.form['dojo_id']
    }
    ninja_id = Ninja.save(data)
    return redirect('/dojos')

# @app.route('/dojos/<int:id>')
# def show_author(id):
#     data = {
#         "id": id
#     }
#     return render_template('show_author.html',dojo=Dojo.get_by_id(data),)