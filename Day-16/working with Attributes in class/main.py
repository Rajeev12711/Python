class User:

    def __init__(self, user_id, user_name):
        self.id = user_id
        self.name = user_name
        self.followers = 0

user1 = User("001","Rajeev")
user2 = User("002", "Gupta")

print(user2.id)
print(user1.name)
print(user2.followers)
