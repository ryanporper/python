# Settinhg up a flask app
- Create a project folder
- Navigate to folder
```py
cd "project_name"
```
- Install our environment
```py
python -m pipenv install flask pymysql flask-bcrypt
```
`WARNING` make sure __pipfile and __pipefile.lock__ our installed
- Launch shell
```py
python -m pipenv shell
```
## Build file structure
```
- flask_app
    - config
        - mysqlconnection.py
    - controllers
        - controller_filename.py
    - model
        - model.py
    - static
        - css
            - style.css
        - js
            - script.js
    - templates
        - index.html 
        - table_name_action.py
        - user_new.html
        - user_edit.html
    - \_\_init__.py
- pipfile
- pipfile.lock
- server.py
```
## mysqlconnection.py
```py
# a cursor is the object we use to interact with the database
import pymysql.cursors

# this class will give us an instance of a connection to our database
class MySQLConnection:
    def __init__(self, db):
        connection = pymysql.connect(host = 'localhost',
                                    user = 'root', # change the user and password as needed
                                    password = 'root', 
                                    db = db,
                                    charset = 'utf8mb4',
                                    cursorclass = pymysql.cursors.DictCursor,
                                    autocommit = True)
        # establish the connection to the database
        self.connection = connection

    # the method to query the database
    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)

                executable = cursor.execute(query)
                if query.lower().find("insert") >= 0:
                    # INSERT queries will return the ID NUMBER of the row inserted
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    # SELECT queries will return the data from the database as a LIST OF DICTIONARIES
                    result = cursor.fetchall()
                    return result
                else:
                    # UPDATE and DELETE queries will return nothing
                    self.connection.commit()
            except Exception as e:
                # if the query fails the method will return FALSE
                print("Something went wrong", e)
                return False
            finally:
                # close the connection
                self.connection.close() 
# connectToMySQL receives the database we're using and uses it to create an instance of MySQLConnection
def connectToMySQL(db):
    return MySQLConnection(db)
```
## controller_user.py
```py
from flask.app import app
from flask import render_template, redirect, session, request
# change this to your model(s)
from flask_app.models import model_table_name

# Default Route
@app.route('/')
def index():
    return redirect('/name')

# Display Route
@app.route('/name')
def names():
    return render_template('name.html')

# Action Route
@app.route('/create/name',methods=['POST'])
def create_name():
    data = {
        "name": request.form['name']
    }
    name_id = Name.save(data)
    return redirect('/name')

# Display Route
@app.route('/name/<int:id>')
def show_name(id):
    return render_template('show_name.html')

# Display Route
@app.route('/name/<int:id>/edit')
def edit_name(id):
    return render_template('edit_name.html')

# Action Route
@app.route('/name/<int:id>/update')
def update_name(id):
    return redirect('/')
    
# Action Route
@app.route('/name/<int:id>/delete')
def delete_name(id):
    return redirect('/')
```

## model_user.py
```py

# finish writing all this later from https://www.youtube.com/watch?v=Su7_0SNazoQ&ab_channel=TylerThibault

# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# from flask_app import DATABASE

DATABASE = "DB_NAME"

# model the class after the DB table from our database
# CHANGE TABLE_NAME TO DB NAME(S)
class table_name:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # C
    @classmethod
    def create(cls, data:dict) -> int:
        query = "INSERT INTO table_name (column_name) VALUES (%(column_name)s);"
        return connectToMySQL('DATABASE').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('DATABASE').query_db(query) # **CHANGE TO DB NAME**
        # Create an empty list to append our instances of friends
        friends = []
        # Iterate over the db results and create instances of friends with cls.
        for friend in results:
            friends.append( cls(friend) )
        return friends
```

