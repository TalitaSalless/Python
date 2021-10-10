cont = soma = 0
while True:
    n = int(input('Digite um número [999 para parar]: '))
    cont += 1
    if n == 999:    #flag
        break
    soma += n
print(f'Voce digitou {cont} números e a soma deles é {soma}')
