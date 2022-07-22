from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    #creates the instance of ninja
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        # self.dojo_id = data['dojo_id']

    @classmethod
    # saves our inputs to the database using a query
    def save(cls, data):
        query ="INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s,%(dojo_id)s);"
        return connectToMySQL('dojo_and_ninjas_schema').query_db(query,data)

