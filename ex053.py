frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('A frase {} invertida fica {}'.format(junto, inverso))
if inverso == junto:
    print('A frase é um palíndromo!')
else:
    print('A frase não é um palíndromo!')
