estudiantes = [
    {"name": "Ana", "grade": 9},
    {"name": "Luis", "grade": 6},
    {"name": "Carlos", "grade": 8},
    {"name": "Melanie", "grade": 4},
    {"name": "David", "grade": 7.5},
    {"name": "Sofía", "grade": 5}
]

aprobados = [estudiante["name"] for estudiante in estudiantes if estudiante["grade"] >= 7]

print("--- Estudiantes Aprobados ---")
for nombre in aprobados:
    print(f"- {nombre}")

print(f"\nTotal aprobados: {len(aprobados)}")
