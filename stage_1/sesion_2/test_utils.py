from utils import is_valid_email

correos = [
    "david@gmail.com",
    "mal_correo",
    "sin_arroba.com",
    "@sin_nombre.com",
    "melanie@hotmail.com"
]

for correo in correos:
    if is_valid_email(correo):
        print(f"{correo} -> VÁLIDO")
    else:
        print(f"{correo} -> INVÁLIDO")