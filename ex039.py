from datetime import date
print('''Informe o seu gênero: 
[1] Feminino
[2] Masculino''')
sexo = int(input('Escolha a opção conforme a lista acima: '))
if sexo == 1:
    print('Você não precisa se alistar.')
    quit()
elif sexo != 1 and sexo != 2:
    print('Sua opção não é valida, tente novamente.')
    quit()
else:
    print('Seu alistamento é obrigatório!')
nasc = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Voce tem {} anos, então está na idade exata para se alistar.'.format(idade))
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Voce irá se alistar no ano de {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Já passaram mais de {} anos.'.format(saldo))
    ano = atual - saldo
    print('Voce já deveria ter se alistado em {}.'.format(ano))