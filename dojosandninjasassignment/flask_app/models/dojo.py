from ..config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja


class Dojo:
    db = 'dojos_and_ninjas_schema_db'
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        dojos = []
        results = connectToMySQL(cls.db).query_db(query)
        for row in results:
            dojos.append(cls(row))
        return dojos

    @classmethod
    def save(cls,data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def select_one(cls, data):
        query = "SELECT * FROM dojos WHERE dojos.id=%(id)s"
        return connectToMySQL(cls.db).query_db(query, data)
       
        # result = connectToMySQL(cls.db).query_db(query, data)
        # return cls(result[0])

    @classmethod
    def select_ninjas(cls, data):
        query = "SELECT * FROM ninjas WHERE dojo_id = %(id)s"
        results = connectToMySQL(cls.db).query_db(query, data)
        return [Ninja(i) for i in results]

    # @classmethod
    # def unfavorited_authors(cls,data):
    #     query = "SELECT * FROM authors WHERE authors.id NOT IN ( SELECT author_id FROM favorites WHERE book_id = %(id)s );"
    #     authors = []
    #     results = connectToMySQL('books').query_db(query,data)
    #     for row in results:
    #         authors.append(cls(row))
    #     return authors

    # @classmethod
    # def add_favorite(cls,data):
    #     query = "INSERT INTO favorites (author_id,book_id) VALUES (%(author_id)s,%(book_id)s);"
    #     return connectToMySQL('books').query_db(query,data);


    # @classmethod
    # def get_by_id(cls,data):
    #     query = "SELECT * FROM dojos LEFT JOIN favorites ON dojo.id = favorites.author_id LEFT JOIN books ON books.id = favorites.book_id WHERE authors.id = %(id)s;"
    #     results = connectToMySQL(cls.db).query_db(query,data)

    #     # Creates instance of author object from row one
    #     dojo = cls(results[0])
    #     # append all book objects to the instances favorites list.
    #     for row in results:
    #         # if there are no favorites
    #         if row['dojos.id'] == None:
    #             break
    #         # common column names come back with specific tables attached
    #         data = {
    #             "first_name": row['first_name'],
    #             "last_name": row['last_name'],
    #             "age": row['age'],
    #         }
    #     return dojo