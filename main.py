import funcoes as f

'''
Esse programa solicita ao usúario frase ou palavras 
e exibe na tela a quantidade vogais e consoantes que há nela.
Exemplo: Palavra
Vogais: 3 / Consoantes: 4
'''

frase = input('Digite uma Palavra ou Frase: ')
frase = frase.lower()
vogais, consoantes = f.contar_vogais_consoantes(frase)
print(f'Vogais: {vogais} / Consoantes: {consoantes}')
