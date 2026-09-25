usuarios = [
    {"name": "Ana", "role": "admin"},
    {"name": "Luis", "role": "student"},
    {"name": "Carlos", "role": "admin"},
    {"name": "Melanie", "role": "teacher"},
    {"name": "David", "role": "student"},
    {"name": "Sofía", "role": "admin"}
]

roles_unicos = []

for usuario in usuarios:
    if usuario["role"] not in roles_unicos:
        roles_unicos.append(usuario["role"])

print("--- Roles únicos encontrados ---")
for rol in roles_unicos:
    print(f"- {rol}")

print(f"\nTotal de roles distintos: {len(roles_unicos)}")
