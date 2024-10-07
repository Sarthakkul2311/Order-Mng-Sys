class User:
    def __init__(self, userId, username, password, role):
        self.userId = userId
        self.username = username
        self.password = password
        self.role = role

    def __str__(self):
        return f"User: {self.username}, Role: {self.role}"
