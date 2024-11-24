def contar_vogais(palavra):
    vogais = "aeiouáéíóúâêîôûãõàèìòù"
    palavra = palavra.lower()
    contador = 0
    for letra in palavra:
        if letra in vogais:
            contador += 1
    return contador