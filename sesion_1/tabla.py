numero = int(input("Ingresa un número para ver su tabla: "))

print(f"\n--- Tabla del {numero} ---")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    