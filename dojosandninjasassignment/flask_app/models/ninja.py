from ..config.mysqlconnection import connectToMySQL

class Ninja:
    db = 'dojos_and_ninjas_schema_db'
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        ninjas = []
        results = connectToMySQL(cls.db).query_db(query)
        for row in results:
            ninjas.append(cls(row))
        return ninjas

    @classmethod
    def save(cls,data):
        query = "INSERT INTO ninjas (name) VALUES (%(name)s);"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod 
    def select_one(cls, data):
        query = "SELECT * FROM ninjas WHERE id=%(id)s"
        return connectToMySQL(cls.db).query_db(query, data)
         