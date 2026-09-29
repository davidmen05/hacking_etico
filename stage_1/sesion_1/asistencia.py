estudiantes = [
    {"name": "Ana", "present": True},
    {"name": "Luis", "present": False},
    {"name": "Carlos", "present": True},
    {"name": "Melanie", "present": False},
    {"name": "David", "present": True},
    {"name": "Sofía", "present": False}
]

print("--- Estudiantes Ausentes ---")
for estudiante in estudiantes:
    if estudiante["present"] == False:
        print(f"- {estudiante['name']}")