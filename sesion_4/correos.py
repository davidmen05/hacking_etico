usuarios = [
    {"id": 1, "name": "Ana", "email": "ana@example.com"},
    {"id": 2, "name": "Luis", "email": "luis@example.com"},
    {"id": 3, "name": "Carlos", "email": "carlos@example.com"},
    {"id": 4, "name": "Melanie", "email": "melanie@example.com"},
    {"id": 5, "name": "David", "email": "david@example.com"}
]

correos = [usuario["email"] for usuario in usuarios]

print("--- Lista de Correos ---")
for correo in correos:
    print(f"- {correo}")

print(f"\nTotal de correos: {len(correos)}")
