def contar_vogais_consoantes(texto: str):
    vogais = 'aeiou'
    qtd_vogais = 0
    qtd_consoantes = 0
    for letra in texto:
        if letra.isalpha():
            if letra in vogais:
                qtd_vogais += 1
            else:
                qtd_consoantes += 1
    return qtd_vogais, qtd_consoantes
