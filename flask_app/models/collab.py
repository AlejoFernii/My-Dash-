from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask import flash

class Collab:
    DB = 'mydash'

    def __init__(self,data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.project_id = data['project_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = " INSERT INTO collabs ( user_id, project_id ) VALUES ( %(user_id)s, %(project_id)s ); "

        return connectToMySQL(cls.DB).query_db(query,data)
    
    @classmethod
    def get_collaborators(cls,data):
        query = "SELECT * FROM collabs JOIN users ON collabs.user_id = users.id WHERE collabs.project_id = %(id)s;"

        results = connectToMySQL(cls.DB).query_db(query,data)

        all_users = []
        for row in results:
            # one = cls(row)

            user_data = {
                'id':row['users.id'],
                'first_name':row['first_name'],
                'last_name':row['last_name'],
                'profession':row['profession'],
                'email':row['email'],
                'pw':row['pw'],
                'created_at':row['users.created_at'],
                'updated_at':row['updated_at'],
                'pic_url':row['pic_url'],
            }

            one_user = user.User(user_data)
            

            all_users.append(one_user)
        return all_users

    

    @classmethod
    def destroy(cls,data):
        query = " DELETE FROM collabs WHERE id = %(id)s; "