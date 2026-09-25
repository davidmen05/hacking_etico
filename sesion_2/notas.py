class InvalidGradeError(Exception):
    pass


def validar_nota(nota):
    if nota < 0 or nota > 10:
        raise InvalidGradeError(f"Nota inválida: {nota}. Debe estar entre 0 y 10.")
    return f"Nota válida: {nota}"


notas = [7, 9.5, -1, 11, 8]

for nota in notas:
    try:
        resultado = validar_nota(nota)
        print(resultado)
    except InvalidGradeError as error:
        print(f"Error capturado: {error}")