velocidade = int(input('Qual a velocidade que o carro está? '))
multa = (velocidade - 80) * 7
a = velocidade - 80
if velocidade > 80:
    print('O limite de velocidade é de 80km/h.')
    print('-.-' * 20)
    print('Você foi MULTADO, por estar acima de {:.0f} km do limite!'.format(a))
    print('Sua multa será de R$ 7,00 por km: R${}'.format(multa))
else:
    print('Voce está dentro do limite de velocidade!')
