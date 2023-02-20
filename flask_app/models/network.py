from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask import flash


class Network:
    DB = "mydash"

    def __init__(self, data):
        self.id = data['id']
        self.users_id = data['users_id']
        self.network = data['network']
        self.url = data['url']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO networks (users_id, network, url) VALUES (%(user_id)s, %(network)s, %(url)s)"

        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_all_from_user(cls, data):
        query = "SELECT * FROM networks WHERE users_id = %(user_id)s;"

        results = connectToMySQL(cls.DB).query_db(query, data)

        all_links = []

        for row in results:

            one_link = cls(row)

            all_links.append(one_link)

        return all_links

    @staticmethod
    def validate_network(network):
        is_valid = True
        if len(network['network']) <= 2:
            flash("Network Name is Required.", 'network')
            is_valid = False
        if len(network['url']) <= 5:
            flash("URL is Required.", 'network')
            is_valid = False

        return is_valid
