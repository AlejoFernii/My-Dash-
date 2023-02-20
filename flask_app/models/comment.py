from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user 
from flask import flash, json, url_for


class Comment:
    DB = 'mydash'

    def __init__(self,data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.convo_id = data['convo_id']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.creator = None
        self.replies = []
    
    

    @classmethod
    def save(cls,data):
        query = " INSERT INTO comments ( user_id, convo_id, comment ) VALUES ( %(user_id)s, %(convo_id)s, %(comment)s ); "

        return connectToMySQL(cls.DB).query_db(query,data)
    
    @classmethod
    def get_all_from_convo(cls,data):
        query = "SELECT * FROM comments JOIN users ON comments.user_id = users.id WHERE comments.convo_id = %(convo_id)s;"

        results = connectToMySQL(cls.DB).query_db(query,data)

        all_comments = []
        for row in results:

            one_comment = cls(row)

            user_data = {
                'id':row['users.id'],
                'first_name':row['first_name'],
                'last_name':row['last_name'],
                'profession':row['profession'],
                'email':row['email'],
                'pw':row['pw'],
                'created_at':row['users.created_at'],
                'updated_at':row['users.updated_at'],
                'pic_url':row['pic_url'],
            }

            one_user = user.User(user_data)
            one_comment.creator = one_user
            date_data = {'id': row['id']}
            posted_at = cls.get_time_posted(date_data)
            one_comment.created_at = posted_at
            all_comments.append(one_comment)
        return all_comments
    
    @classmethod
    def get_time_posted(cls,data):
        query = "SELECT DATE_FORMAT(created_at, '%%%%a %%%%r') AS date FROM comments WHERE id = %(id)s;"

        result = connectToMySQL(cls.DB).query_db(query,data)

        return result[0]['date']
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM comments JOIN users ON comments.user_id = users.id WHERE comment = %(comment)s AND user_id = %(user_id)s;"

        result = connectToMySQL(cls.DB).query_db(query,data)

        for row in result:
            one_comment = cls(row)

            user_data = {
                'id':row['users.id'],
                'first_name':row['first_name'],
                'last_name':row['last_name'],
                'profession':row['profession'],
                'email':row['email'],
                'pw':row['pw'],
                'created_at':row['users.created_at'],
                'updated_at':row['users.updated_at'],
                'pic_url':row['pic_url'],
            }

            one_user = user.User(user_data)
            one_comment.creator = one_user

            pic = url_for('static',filename=f'/uploads/{one_comment.creator.pic_url}')
            one_comment.creator.pic_url = pic

            date_data = {'id': row['id']}
            posted_at = cls.get_time_posted(date_data)
            one_comment.created_at = posted_at
            
            return one_comment



    @classmethod
    def destroy(cls,data):
        query = " DELETE FROM comments WHERE id = %(id)s; "

        return connectToMySQL(cls.DB).query_db(query,data)