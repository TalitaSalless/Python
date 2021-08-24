from random import randint
from time import sleep
itens = 'Pedra', 'Papel', 'Tesoura'
computador = randint(0, 2)
nome = str(input('Qual o seu nome? '))
print('''Suas opções são:
[0] Pedra
[1] Papel 
[2] Tesoura''')
jogador = int(input('Escolha uma opção: '))
print('Lá vai....')
sleep(1)
print('\033[34mJÔ...\033[m')
sleep(1)
print('\033[34mKEN...\033[m')
sleep(1)
print('\033[34mPÔ!!\033[m')
sleep(1)
print('-=-' * 8)
print('Você {} escolheu {}'.format(nome, itens[jogador]))
print('\033[33mO Computador escolheu {}\033[m'.format(itens[computador]))
print('-=-' * 8)
if computador == 0:      #PEDRA
    if jogador == 0:
        print('EMPATOU')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('Jogada Inválida!')
elif computador == 1:     #PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('EMPATOU')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    else:
        print('Jogada Inválida!')
elif computador == 2:    #TESOURA
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATOU')
    else:
        print('Jogada Inválida!')
