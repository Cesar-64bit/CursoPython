def es_palindormo(texto):
    palindromo = True
    texto.replace(" ", "").lower()

    for i in range(len(texto)):
        if texto[i] != texto[-i-1]:
            palindromo = False
            break

    return palindromo


print("abba ", es_palindormo("abba"))
