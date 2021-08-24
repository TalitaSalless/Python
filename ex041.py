from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Voce é da CATEGORIA MIRIM')
elif idade <= 14:
    print('Voce é da CATEGORIA INFANTIL')
elif idade <= 19:
    print('Voce é da CATEGORIA JÚNIOR')
elif idade <= 25:
    print('Voce é da CATEGORIA SÊNIOR')
else:
    print('Voce é da CATEGORIA MASTER')






