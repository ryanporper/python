# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
from flask_app import app
from flask import render_template
# model the class after the dojo table from our database
class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojos_and_ninjas_schema_db').query_db(query)
        # Create an empty list to append our instances of dojos
        dojos = []
        # Iterate over the db results and create instances of dojos with cls.
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

@app.route("/")
def index():
    # call the get all classmethod to get all dojos
    dojos = Dojo.get_all()
    print(dojos)
    return render_template("dojo.html", dojos = dojos)