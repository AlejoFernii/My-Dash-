from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask import flash


class Function:
    DB = "mydash"

    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.name = data['name']
        self.location = data['location']
        self.date = data['date']
        self.attire = data['attire']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.creator = None
        self.attendees = []

    @classmethod
    def save(cls, data):
        query = """INSERT INTO functions ( user_id, name, location, date, attire, description )
                    VALUES ( %(user_id)s, %(name)s, %(location)s,DATE_FORMAT(%(date)s, ' %%%%D %%%%M %%%%Y ') , %(attire)s, %(description)s );"""

        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_all_with_user(cls):
        query = "SELECT * FROM functions JOIN users ON functions.user_id = users.id;"

        results = connectToMySQL(cls.DB).query_db(query)
        all_functions = []
        for row in results:
            one_function = cls(row)

            user_data = {
                'id': row['users.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'profession': row['profession'],
                'email': row['email'],
                'pw': row['pw'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at'],
                'pic_url': row['pic_url'],
            }

            one_user = user.User(user_data)
            one_function.creator = one_user

            all_functions.append(one_function)

        return all_functions
    
    @classmethod
    def get_one_with_user(cls,data):
        query = "SELECT * FROM functions JOIN users ON functions.user_id = users.id WHERE functions.id = %(id)s;"

        result = connectToMySQL(cls.DB).query_db(query,data)

        for row in result:
            one_function = cls(row)

            user_data = {
                'id': row['users.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'profession': row['profession'],
                'email': row['email'],
                'pw': row['pw'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at'],
                'pic_url': row['pic_url'],
            }

            one_user = user.User(user_data)
            one_function.creator = one_user


        return one_function
    
    @classmethod
    def update_function(cls,data):
        query = "UPDATE functions SET name = %(name)s, date = %(date)s, location = %(location)s, description = %(description)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.DB).query_db(query,data)

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM functions WHERE id = %(id)s;"

        return connectToMySQL(cls.DB).query_db(query, data)


    @staticmethod
    def validate_function(function):
        is_valid = True
        if len(function['name']) <= 2 :
            flash("Event Name is Required.",'function')
            is_valid = False
        if len(function['date']) <= 5 :
            flash("Date is Required.", 'function')
            is_valid = False
        if len(function['location']) <= 0 :
            flash("Location is Required.",'function')
            is_valid = False
        if len(function['attire']) <= 3 :
            flash("Attire is Required.", 'function')
            is_valid = False
        if len(function['description']) <= 10 :
            flash("Please Describe the Event.", 'function')
            is_valid = False
        
        return is_valid