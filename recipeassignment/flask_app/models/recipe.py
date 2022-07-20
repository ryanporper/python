from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.user import User

db_name = 'recipes'

class Recipe:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date = data['date']
        self.under = data['under']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes JOIN users on users.id = user_id;"
        result = connectToMySQL(db_name).query_db(query)
        recipes = []
        for row_from_db in result:
            current_recipe = cls(row_from_db)
            user_data = {
                **row_from_db,
                'id': row_from_db['users.id'],
                'created_at': row_from_db['users.created_at'],
                'updated_at': row_from_db['users.updated_at']
            }
            recipes_user = User(user_data)
            current_recipe.owner = recipes_user
            recipes.append(current_recipe)
        return recipes

    @classmethod
    def get_one_by_id(cls,data):
        query = "SELECT * FROM recipes JOIN users on users.id = user_id WHERE recipes.id = %(id)s;"
        result = connectToMySQL(db_name).query_db(query,data)
        recipe = cls(result[0])
        row_from_db = result[0]

        user_data = {
            **row_from_db,
            'id': row_from_db['users.id'],
            'created_at': row_from_db['users.created_at'],
            'updated_at': row_from_db['users.updated_at']
        }
        owner = User(user_data)
        recipe.owner = owner
        return recipe

    @classmethod
    def delete_by_id(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s"
        return connectToMySQL(db_name).query_db(query, data)

    @classmethod
    def save(cls,data):
        query = "INSERT INTO recipes (name, description, instructions, date, under, user_id) VALUES(%(name)s, %(description)s, %(instructions)s, %(date)s, %(under)s,%(user_id)s)"
        return connectToMySQL(db_name).query_db(query,data)

    @classmethod
    def update(cls,data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date = %(date)s, under = %(under)s, user_id = %(user_id)s WHERE id = %(id)s"
        return connectToMySQL(db_name).query_db(query,data)

    @staticmethod
    def is_valid(data):
        is_valid = True
        if len(data['name']) < 3:
            is_valid = False
            flash("Recipe name must be at least 3 characters.","new")
        if len(data['description']) < 3:
            is_valid = False
            flash("Description must be at least 3 characters.","new")
        if len(data['instructions']) < 3:
            is_valid = False
            flash("Instructions must be at least 3 characters.","new")
        if len(data['date']) < 1:
            is_valid = False
            flash("You must enter a date.","new")
        return is_valid


    
        

