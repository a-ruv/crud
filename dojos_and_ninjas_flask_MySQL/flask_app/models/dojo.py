from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    #creates the instance of dojo
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.ninjas = []

    @classmethod #saves our inputs to the database using a query
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        return connectToMySQL('dojo_and_ninjas_schema').query_db(query, data)
        
    @classmethod #gets all our dojos table info
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojo_and_ninjas_schema').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

    @classmethod #gets all ninjas info that are in that certain dojo
    def get_dojo_with_ninjas(cls,data):
        query ="SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL("dojo_and_ninjas_schema").query_db(query,data)
        dojo = cls(results[0])
        for row in results:
            ninja_data = {
                "id": row["ninjas.id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "age": row["age"]
            }
            dojo.ninjas.append(ninja.Ninja(ninja_data))
            print(ninja_data["first_name"])
        return dojo