def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


try:
    opcion = input("¿Qué quieres convertir? (C para Celsius a Fahrenheit, F para Fahrenheit a Celsius): ").upper()

    if opcion == "C":
        celsius = float(input("Ingresa los grados Celsius: "))
        resultado = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C = {resultado:.2f}°F")
    elif opcion == "F":
        fahrenheit = float(input("Ingresa los grados Fahrenheit: "))
        resultado = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F = {resultado:.2f}°C")
    else:
        print("Opción no válida. Debe ser C o F.")

except ValueError:
    print("Error: Debes ingresar un número válido.")