soma = cont = media = maior = menor = 0
resp = 'S'
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    resp = str(input('Quer continuar?: [S/N]')).upper().strip()[0]
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / cont
print('Voce digitou {} números e a média foi {}'.format(cont, media))
print('O maior número é {} e o menor número é {}'.format(maior, menor))
