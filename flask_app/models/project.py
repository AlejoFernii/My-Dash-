from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user, collab 
from flask import flash

class Project:
    DB = "mydash"
    def __init__(self,data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.name = data['name']
        self.skills = data['skills']
        self.type = data['type']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.creator = None
        self.collaborators = []


    @classmethod
    def save(cls,data): 
        query = """ INSERT INTO projects ( user_id, name, skills, type, description ) 
                    VALUES ( %(user_id)s, %(name)s, %(skills)s, %(type)s, %(description)s ); """
        return connectToMySQL(cls.DB).query_db(query,data)
    

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM projects JOIN users ON projects.user_id = users.id WHERE projects.id = %(id)s;"

        result = connectToMySQL(cls.DB).query_db(query,data)

        one_project = cls(result[0])

        user_data = {
                'id': result[0]['users.id'],
                'first_name': result[0]['first_name'],
                'last_name': result[0]['last_name'],
                'profession': result[0]['profession'],
                'email': result[0]['email'],
                'pw': result[0]['pw'],
                'created_at': result[0]['created_at'],
                'updated_at': result[0]['updated_at'],
                'pic_url': result[0]['pic_url'],
            }

        one_user = user.User(user_data)
        one_project.creator = one_user

        return one_project


    

    @classmethod
    def get_all_from_user(cls,data):
        query = " SELECT * FROM projects JOIN users ON projects.user_id = users.id WHERE users.id = %(id)s;"


        results = connectToMySQL(cls.DB).query_db(query,data)
        all_projects = []
        for row in results:
            one_project = cls(row)

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
            one_project.creator = one_user

            all_projects.append(one_project)

        return all_projects


    @classmethod
    def update_project(cls,data):
        query = "UPDATE projects SET name = %(name)s, skills = %(skills)s, type = %(type)s, description = %(description)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.DB).query_db(query,data)

    @classmethod
    def destroy(cls,data):
        query = " DELETE FROM projects WHERE id = %(id)s; "

        return connectToMySQL(cls.DB).query_db(query,data)
    
    @staticmethod
    def validate_project(project):
        is_valid = True
        if len(project['name']) <= 2 :
            flash("Project Name is Required.",'project')
            is_valid = False
        if len(project['skills']) <= 5 :
            flash("Skill(s) used is Required.", 'project')
            is_valid = False
        if len(project['type']) <= 0 :
            flash("Project Type is Required.",'project')
            is_valid = False
        if len(project['description']) <= 10 :
            flash("Please Describe your Project.", 'project')
            is_valid = False
        
        return is_valid