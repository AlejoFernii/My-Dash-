from flask_app.config.mysqlconnection import connectToMySQL
# from flask_app.models import 
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    DB = 'mydash'

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.profession = data['profession']
        self.email = data['email']
        self.pw = data['pw']

        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.pic_url = data['pic_url']
        self.is_admin = False
        self.convos = []

    @classmethod
    def create(cls, data):
        query = """ INSERT INTO users (first_name, last_name, email, pw, created_at, updated_at)
                    VALUES (%(first_name)s, %(last_name)s, %(email)s, %(pw)s, NOW(),NOW()); """

        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id=%(id)s;"

        result = connectToMySQL(cls.DB).query_db(query, data)

        return cls(result[0])
    
    @classmethod
    def get_user_with_convos(cls,data):
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
    def get_all(cls):
        query = "SELECT * FROM users;"
        return connectToMySQL(cls.DB).query_db(query)

    # @classmethod
    # def get_by_username(cls,data):
    #     query = "SELECT * FROM users WHERE username = %(username)s;"
    #     result = connectToMySQL('wall').query_db(query,data)
    #     if len(result) < 1:
    #         return False
    #     return cls(result[0])

    @classmethod
    def update_Profession(cls,data):
        query="UPDATE users SET profession = %(profession)s WHERE id = %(id)s;"
        return connectToMySQL(cls.DB).query_db(query,data)

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(cls.DB).query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])
    
    @classmethod
    def save_user_pic(cls,data):
        query = "UPDATE users SET pic_url = %(pic_url)s WHERE id = %(id)s;"
        return connectToMySQL(cls.DB).query_db(query,data)

    @classmethod
    def get_user_pic(cls,data):
        query = "SELECT pic_url FROM users WHERE id = %(id)s;"

        result = connectToMySQL(cls.DB).query_db(query,data)
        pic = result[0]['pic_url']
        return pic

    @staticmethod
    def validate(member):
        is_valid = True
        if len(member['first_name']) <= 2:
            flash("First Name Required.", 'reg')
            is_valid = False
        if len(member['last_name']) <= 2:
            flash("Last Name Required.", 'reg')
            is_valid = False
        if len(member['pw']) < 8:
            flash("Password Must Be At Least 8 Characters.", 'reg')
            is_valid = False
        if not EMAIL_REGEX.match(member['email']):
            flash("Invalid Email Format.", 'reg')
            is_valid = False
        if member['conpw'] != member['pw']:
            flash("Password Must Match.", 'reg')
            is_valid = False
        return is_valid
