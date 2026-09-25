def find_user_by_email(users, email):
    return next((user for user in users if user["email"] == email), None)


usuarios = [
    {"id": 1, "name": "Ana", "email": "ana@example.com"},
    {"id": 2, "name": "Luis", "email": "luis@example.com"},
    {"id": 3, "name": "Carlos", "email": "carlos@example.com"},
    {"id": 4, "name": "Melanie", "email": "melanie@example.com"},
    {"id": 5, "name": "David", "email": "david@example.com"}
]

resultado1 = find_user_by_email(usuarios, "carlos@example.com")
print(f"Búsqueda 1: {resultado1}")

resultado2 = find_user_by_email(usuarios, "noexiste@example.com")
print(f"Búsqueda 2: {resultado2}")