class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def add_users_db(self):
        return [self.name, self.user_id]
