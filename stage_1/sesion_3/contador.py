class User:
    total_usuarios = 0

    def __init__(self, name, email):
        self.name = name
        self.email = email
        User.total_usuarios += 1

    def display(self):
        return f"Name: {self.name} | Email: {self.email}"


user1 = User("Lucas", "lucas.romero@gmail.com")
user2 = User("Melanie", "vera.abad@gmail.com")
user3 = User("David", "mendoza@gmail.com")

print(user1.display())
print(user2.display())
print(user3.display())

print(f"\nTotal de usuarios creados: {User.total_usuarios}")