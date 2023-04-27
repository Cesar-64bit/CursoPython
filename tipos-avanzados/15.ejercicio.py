string = "Hola mundo este es mi string"


def quita_espacios(texto):
    '''Retorna una cadena de caracteres sin espacios'''
    return [char for char in texto if char != " "]


def cuenta_caracteres(lista):
    '''Retorna la cantidad de caracteres que se repiten en la cadena'''
    chars_dict = {}
    for char in lista:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict


def ordena(dict):
    '''Ordena de manera descendente la cantidad de caracteres que se repiten'''
    return sorted(
        dict.items(),
        key=lambda key: key[1],
        reverse=True,
    )


def mayores_tuplas(lista):
    '''Retorna los caracteres con mayor repeticiones'''
    maximo = lista[0][1]
    respuesta = {}
    for orden in lista:
        if maximo > orden[1]:
            break
        respuesta[orden[0]] = orden[1]
    return respuesta


def crea_mensaje(diccionario):
    '''Retorna una cadena de texto que indica la cantidad de repeticiones de cada caracter'''
    mensaje = "Los que más se repite son: \n"
    for key, valor in diccionario.items():
        mensaje += f"- {key} con {valor} repeticiones \n"
    return mensaje


sin_espacios = quita_espacios(string)
contados = cuenta_caracteres(sin_espacios)
ordenados = ordena(contados)
mayores = mayores_tuplas(ordenados)
mensaje = crea_mensaje(mayores)
print(mensaje)
