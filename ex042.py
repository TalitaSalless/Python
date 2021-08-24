r1 = float(input('Digite o primeiro comprimento: '))
r2 = float(input('Digite o segundo comprimento: '))
r3 = float(input('Digite o terceiro comprimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo:', end=' ')
    if r1 == r2 == r3:
        print('EQUILÁTERO, todos os lados iguais!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO, todos os lados diferentes')
    else:
        print('ISÓSCELES, dois lados iguais, um diferente!')
else:
    print("Os segmentos acima não podem formar um triângulo!")

