from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Survey:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data): #todo name of table(dojos)
        query = "INSERT into dojos (name, location, language, comment) VALUES (%(name)s,%(location)s,%(language)s,%(comment)s);"
                #todo name of database(dojo_survey_schema)
        return connectToMySQL('dojo_survey_schema').query_db(query,data)
                            

    @classmethod
    def get_last_survey(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojo_survey_schema').query_db(query)
        return results

    @staticmethod
    def is_valid(survey):
        is_valid = True
        if len(survey['name']) < 3:
            is_valid = False
            flash("Name must be at least 3 characters.")
        if len(survey['location']) < 3:
            is_valid = False
            flash("Location must be at least 1 characters.")
        if len(survey['language']) < 1:
            is_valid = False
            flash("Language must be at least 1 characters.")
        if len(survey['comment']) < 1:
            is_valid = False
            flash("Comments must be at least 3 characters.")   
        return is_valid

    

        

    