def logger(funcion):
    def wrapper(*args, **kwargs):
        print(f"Ejecutando: {funcion.__name__}")
        print(f"  args: {args} | kwargs: {kwargs}")
        return funcion(*args, **kwargs)
    return wrapper


@logger
def sumar(a, b):
    return a + b


@logger
def presentar(nombre, edad):
    return f"Hola {nombre}, tienes {edad} años"


print(sumar(5, 3))
print(presentar(nombre="David", edad=22))