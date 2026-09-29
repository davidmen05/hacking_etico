usuarios = [
    {"id": 1, "name": "Ana", "email": "ana@gmail.com"},
    {"id": 2, "name": "Luis", "email": "luis@gmail.com"},
    {"id": 3, "name": "Carlos", "email": "carlos@gmail.com"},
    {"id": 4, "name": "Melanie", "email": "melanie@gmail.com"},
    {"id": 5, "name": "David", "email": "david@gmail.com"}
]

correos = [usuario["email"] for usuario in usuarios]

print("--- Lista de Correos ---")
for correo in correos:
    print(f"- {correo}")

print(f"\nTotal de correos: {len(correos)}")
