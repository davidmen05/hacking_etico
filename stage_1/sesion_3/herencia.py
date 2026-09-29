class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display(self):
        return f"Name: {self.name} - Email: {self.email}"

user1 = User("Lucas", "Lucas.romero@gmail.com")
user2 = User("Melanie", "melanie.vera@gmail.com")
user3 = User("David", "david.mendoza@gmail.com")

print(user1.display())
print(user2.display())
print(user3.display())

class Admin(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.role = 'admin'

    def display(self):
        return f"{self.name}, {self.email}, {self.role}"

user4 = Admin("AdminUser", "adminuser@gmail.com")
user5 = Admin("AdminUser2", "adminuser2@gmail.com")

print(user4.display())
print(user5.display())