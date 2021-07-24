ano = int(input('Digite um ano: '))
if ano % 4 == 0:
    print('O {} é bissexto!'.format(ano))
else:
    print('O {} não é bissexto!'.format(ano))