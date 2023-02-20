from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user, comment 
from flask import flash

class Convo:
    DB = 'mydash'
    def __init__(self,data):
        self.id = data['id']
        self.user_id =data['user_id']
        self.topic = data['topic']
        self.convo_starter = data['convo_starter']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.creator = None
        self.comments = []


    @classmethod
    def save(cls,data):
        query = "INSERT INTO convos ( user_id, topic, convo_starter ) VALUES ( %(user_id)s, %(topic)s, %(convo_starter)s );"

        return connectToMySQL(cls.DB).query_db(query,data)
    

    @classmethod
    def get_all_with_comments(cls):
        query = "SELECT * FROM convos JOIN users ON convos.user_id = users.id;"

        results = connectToMySQL(cls.DB).query_db(query)

        all_convos = []

        for row in results:

            one_convo = cls(row)

            user_data = {
                'id':row['users.id'],
                'first_name':row['first_name'],
                'last_name':row['last_name'],
                'email':row['email'],
                'profession':row['profession'],
                'pw':row['pw'],
                'created_at':row['created_at'],
                'updated_at':row['updated_at'],
                'pic_url':row['pic_url'],
            }

            one_user = user.User(user_data)
            one_convo.creator = one_user
            date_data = {'id':row['id']}
            posted_at = cls.get_time_posted(date_data) 
            one_convo.created_at = posted_at
            all_convos.append(one_convo)

        return all_convos


    @classmethod
    def get_time_posted(cls,data):
        query = "SELECT DATE_FORMAT(created_at, '%%%%a %%%%r') AS date FROM convos WHERE id = %(id)s;"

        result = connectToMySQL(cls.DB).query_db(query,data)

        return result[0]['date']


    @classmethod
    def get_all_from_user(cls,data):
        query = "SELECT * FROM convos JOIN users ON convos.user_id = users.id WHERE users.id = %(id)s;"

        results = connectToMySQL(cls.DB).query_db(query,data)

        all_convos = []

        for row in results:

            one_convo = cls(row)

            user_data = {
                'id':row['users.id'],
                'first_name':row['first_name'],
                'last_name':row['last_name'],
                'email':row['email'],
                'profession':row['profession'],
                'pw':row['pw'],
                'created_at':row['created_at'],
                'updated_at':row['updated_at'],
                'pic_url':row['pic_url'],
            }

            one_user = user.User(user_data)
            one_convo.creator = one_user
            date_data = {'id':row['id']}
            posted_at = cls.get_time_posted(date_data) 
            one_convo.created_at = posted_at
            convo_id = {
                'convo_id':row['id']
            }
            all_comments = comment.Comment.get_all_from_convo(convo_id)
            for one_comment in all_comments:
                one_convo.comments.append(one_comment)

            all_convos.append(one_convo)

        return all_convos
    

    @classmethod
    def get_one_with_comments(cls,data):
        query = "SELECT * FROM convos JOIN users ON convos.user_id = users.id WHERE convos.id = %(id)s;"

        result = connectToMySQL(cls.DB).query_db(query,data)


        for row in result:

            one_convo = cls(row)

            user_data = {
                'id':row['users.id'],
                'first_name':row['first_name'],
                'last_name':row['last_name'],
                'email':row['email'],
                'profession':row['profession'],
                'pw':row['pw'],
                'created_at':row['users.created_at'],
                'updated_at':row['users.updated_at'],
                'pic_url':row['pic_url'],
            }

            one_user = user.User(user_data)
            one_convo.creator = one_user
            date_data = {'id':row['id']}
            posted_at = cls.get_time_posted(date_data) 
            one_convo.created_at = posted_at
            convo_id = {
                'convo_id':row['id']
            }
            
            all_comments = comment.Comment.get_all_from_convo(convo_id)
            for one_comment in all_comments:

                one_convo.comments.append(one_comment)


        return one_convo


    @classmethod
    def update_convo(cls,data):
        query = "UPDATE convos SET topic = %(topic)s, convo_starter = %(convo_starter)s WHERE id = %(id)s;"

        return connectToMySQL(cls.DB).query_db(query,data)



    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM convos WHERE id = %(id)s;"

        return connectToMySQL(cls.DB).query_db(query,data)


    @staticmethod
    def validate_convo(convo):
        is_valid = True
        if len(convo['topic']) <= 0 :
            flash("Topic is Required.",'convo')
            is_valid = False
        if len(convo['convo_starter']) <= 0 :
            flash("Conversation Starter is Required.", 'convo')
            is_valid = False
        
        return is_valid
