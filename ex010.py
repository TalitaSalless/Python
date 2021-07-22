carteira = float(input('Digite o valor que voce tem na carteira: R$ '))
dolar = carteira / 4.91
euro = carteira / 5.86
peso = carteira / 0.05
print(f'Voce podera comprar em:\nUS$ {dolar:.2f} doláres \n€ {euro:.2f} euros \n$ {peso:.2f} pesos argentinos')
