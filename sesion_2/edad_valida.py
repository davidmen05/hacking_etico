def pedir_edad():
    while True:
        try:
            edad = int(input("Ingresa tu edad (0-120): "))
            if 0 <= edad <= 120:
                return edad
            else:
                print("Edad fuera de rango. Intenta de nuevo.")
        except ValueError:
            print("Error: Debes ingresar un número entero.")


edad = pedir_edad()
print(f"Tu edad es: {edad}")