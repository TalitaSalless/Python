sexo = str(input('Qual o seu sexo? [F/M]')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados INVÁLIDOS. Digite novamente seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
