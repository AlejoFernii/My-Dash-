from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask import flash


class Skill:
    DB = "mydash"

    def __init__(self, data):
        self.id = data['id']
        self.skill = data['skill']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def save(cls,data):
        query="INSERT INTO skills (skill) VALUES (%(skill)s);"

        return connectToMySQL(cls.DB).query_db(query,data)



    @classmethod
    def add_skill_to_user(cls,data):
        query = "INSERT INTO user_skills (skill_id, user_id) VALUES (%(skill_id)s, %(user_id)s);"

        return connectToMySQL(cls.DB).query_db(query,data)
    

    @classmethod
    def get_all_from_user(cls,data):
        query = "SELECT * FROM user_skills JOIN skills ON user_skills.skill_id = skills.id WHERE user_skills.user_id = %(user_id)s;"

        results = connectToMySQL(cls.DB).query_db(query,data)

        all_skills = []
        for row in results:
            skill_data = {
                'id': row['skills.id'],
                'skill': row['skill'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at'],
            }
            one_skill = cls(skill_data)

            all_skills.append(one_skill)

        return all_skills



    @classmethod
    def get_skill_by_name(cls,data):
        query = "SELECT * FROM skills WHERE skill = %(skill)s;"

        results = connectToMySQL(cls.DB).query_db(query,data)
        
        one_skill = cls(results[0])

        return one_skill
    

    @staticmethod
    def validate_skill(skill):
        is_valid = True
        if len(skill['skill']) <= 2:
            flash("Skill is Required.", 'skill')
            is_valid = False

        return is_valid