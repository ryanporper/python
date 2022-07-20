from pyexpat import model
from flask import render_template, session, redirect, request, flash
from flask_app import app
from flask_app.models.recipe import Recipe
from flask_app.models.user import User

@app.route('/recipes/new')
def recipe_new():
    if 'id' not in session:
        flash('Log in before trying to view the dashboard.')
        return redirect('/')
    return render_template("new_recipe.html")

@app.route('/recipes/create', methods=['POST'])
def recipe_create():
    if not Recipe.is_valid(request.form):
        return redirect('/recipes/new')
    if "under" not in request.form:
        data = {
             **request.form,
            "id": id,
            "under": '0'
        }
    else:
        data = {
            **request.form,
            'id': session['id']
        }
    Recipe.save(data)
    return redirect('/dashboard')

@app.route('/recipes/<int:id>/view')
def show_one_recipe(id):
    if 'id' not in session:
        flash('Log in before trying to view the dashboard.')
        return redirect('/')
    data = {'id': id}
    recipe = Recipe.get_one_by_id(data)
    return render_template("show_recipe.html", recipe=recipe)

@app.route('/recipes/<int:id>/delete')
def delete_recipe(id):
    data = {
        'id': id
    }
    recipe = Recipe.get_one_by_id(data)
    if recipe.user_id != session['id']:
        flash('Nice try bucko.')
        return redirect('/dashboard')
    Recipe.delete_by_id(data)
    return redirect('/dashboard')

@app.route('/recipes/<int:id>/edit')
def edit_recipe(id):
    data = {
        'id': id
    }
    recipe = Recipe.get_one_by_id(data)
    if recipe.user_id != session['id']:
        flash('Nice try bucko.')
        return redirect('/dashboard')
    return render_template('edit_recipe.html', recipe=recipe)

@app.route('/recipes/<int:id>/update', methods=['POST'])
def update_recipe(id):
    if "under" not in request.form:
        updated_info = {
             **request.form,
            "id": id,
            "under": '0'
        }
    else:
        updated_info = {
            **request.form,
            'id': id
        }
    recipe = Recipe.get_one_by_id(updated_info)
    if recipe.user_id != session['id']:
        flash('Nice try bucko.')
        return redirect('/dashboard')

    if not Recipe.is_valid(updated_info):
        return redirect(f'/recipes/{id}/edit')

    Recipe.update(updated_info)
    return redirect('/dashboard')