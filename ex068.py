from random import randint
v = 0
print('~ \033[31mVAMOS JOGAR PAR OU IMPAR!\033[m ~')
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Você escolhe: PAR ou IMPAR? [P/I] ')).strip().upper()[0]
    print(f'Voce jogou {jogador} e o computador jogou {computador} somando uma total de {total}', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce venceu!')
            v += 1
        else:
            print('Voce perdeu!')
            break
    if tipo == 'I':
        if total % 2 == 1:
            print('Voce venceu!')
            v += 1
        else:
            print('Voce perdeu!')
            break
    print('Vamos Jogar novamente!')
print(f'---Game Over--- Voce venceu {v} partida(s)')
