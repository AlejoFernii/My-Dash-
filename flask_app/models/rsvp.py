from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask import flash

class RSVP:
    DB = 'mydash'

    def __init__(self,data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.function_id = data['function_id']
        self.created_at = data['created_at']

    @classmethod
    def save(cls,data):
        query = " INSERT INTO rsvp ( user_id, function_id ) VALUES ( %(user_id)s, %(function_id)s ); "

        return connectToMySQL(cls.DB).query_db(query,data)


    @classmethod
    def get_all_rsvps(cls,data):
        query = "SELECT * FROM rsvp JOIN users ON rsvp.user_id = users.id WHERE rsvp.function_id = %(function_id)s;"

        results = connectToMySQL(cls.DB).query_db(query,data)

        all_attendees = []

        for row in results:

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
            all_attendees.append(one_user)

        return all_attendees