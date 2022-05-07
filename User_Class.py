from WebApp.db_functions import get_user_id,get_user_id_by_id,get_user_name_by_id,get_user_name_by_email

class userClass:


    def __init__(self,email):
        self.email = email
        self.is_authenticated = True
        self.is_active = True
        self.login_manager = False
        self.is_anonymous = False
        self.name = get_user_name_by_email(self.email)

    def get_id(self):

        unicode_id = get_user_id(self.email)

        return unicode_id





class userClassid:


    def __init__(self,id):
        self.user_id = id
        self.is_authenticated = True
        self.is_active = True
        self.login_manager = False
        self.is_anonymous = False
        self.name = get_user_name_by_id(self.user_id)

    def get_id(self):
        unicode_id = get_user_id_by_id(self.user_id)
        return unicode_id

