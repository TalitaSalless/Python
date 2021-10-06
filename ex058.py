from random import randint
computador = randint(0, 10)
print('Olá eu sou o seu computador, irei pensar em um número de 0 a 10!')
print('Será que voce consegue descobrir?')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite?: '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...Tente novamente: ')
        elif jogador > computador:
            print('Menos...Tente novamente: ')
print('Acertou com {} palpites. Parabens!'.format(palpite))
