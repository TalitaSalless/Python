from random import randint
from time import sleep
computador = randint(0, 5) #computador vai 'pensar'
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em qual número eu pensei? ')) #Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Parabens, acertou o número que eu pensei! =) ')
else:
    print('GANHEI! Eu pensei no número {} e não no {} :) '.format(computador,jogador))
print('-=-' * 20)
print('FIM DE JOGO')


