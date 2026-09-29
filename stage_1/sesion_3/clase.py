class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        print("User created")

    def show_information(self):
        return f"Name: {self.name} Email: {self.email}"

user1 = User("Lucas", "Lucas.romero@gmail.com")
user2 = User("Melanie", "melanie.vera@gmail.com")
user3 = User("David", "david.mendoza@gmail.com")

print(user1.show_information())
print(user2.show_information())
print(user3.show_information())