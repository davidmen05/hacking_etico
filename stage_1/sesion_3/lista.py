users = list()

users.append({"id": 1, "name": "Lucas", "email": "Lucas.romero@gmail.com", "role": "admin"})
users.append({"id": 2, "name": "Melanie", "email": "vera.abad@gmail.com", "role": "user"})
users.append({"id": 3, "name": "David", "email": "mendoza@gmail.com", "role": "admin"})
users.append({"id": 4, "name": "Juan", "email": "cevallos@gmail.com", "role": "admin"})

counter = list()

print("--- Usuarios Administradores ---")
for user in users:
    if user["role"] == "admin":
        counter.append(user) 
        print(f"Name: {user['name']} | Email: {user['email']} | Role: {user['role']}")

print(f"\nTotal Admin Users: {len(counter)}")

usuario_id_3 = next(user for user in users if user["id"] == 3)
print(f"\n[Con next()] Usuario con id 3: {usuario_id_3}")

nombre_id_3 = next(user["name"] for user in users if user["id"] == 3)
print(f"[Con next()] Nombre del usuario con id 3: {nombre_id_3}")