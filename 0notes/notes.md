- Installation
- Mavigate to the project folder then execute this command
```
python -m pipenv install flask pymysql
```
```
python -m pipenv shell
```
- file structure
    - flask_app
        - config
            - mysqlconnection.py
        - controllers
            - controller_filename.py

    - model
    - static
        - css
            - style.css
        - js
            - script.js
        - \_\_init__.py
    - templates
        - index.html
    - pipfile
    - pipfile.lock
    - server.py

FILE TEMPLATES
- mysqlconnection.py file
```py 
# a cursor is the object we use to interact with the database
import pymysql.cursors
# this class will give us an instance of a connection to our database
class MySQLConnection:
    def __init__(self, db):
        # change the user and password as needed
        connection = pymysql.connect(host = 'localhost',
                                    user = 'root', 
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
     
                cursor.execute(query)
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

- model_table_name.py file

```py 
# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the DB table from our database

# CHANGE FRIEND(S) TO DB NAME(S)
class Friend:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('DB_NAME').query_db(query) # **CHANGE TO DB NAME**
        # Create an empty list to append our instances of friends
        friends = []
        # Iterate over the db results and create instances of friends with cls.
        for friend in results:
            friends.append( cls(friend) )
        return friends
```
- server.py file

```py
from flask_app import app
# import every controller file
from flask_app.controllers import controller_dojo
       
if __name__ == "__main__":
    app.run(debug=True)
```

- \_\_init__.py file
```py
from flask import Flask

app = Flask(__name__)
app.secret_key = "supersecret"
```
