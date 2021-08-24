soma = 0
cont = 0
for c in range(1,7):           #ler os 6 numeros
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:      #se forem pares...
        soma += num       #soma os numeros pares
        cont += 1         #conta quantos foram pares
print('Voce informou {} números Pares e a soma foi {}'.format(cont, soma))
