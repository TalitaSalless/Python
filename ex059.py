n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
option = 0
while option != 5:
    print('''Digite o número referente a opção desejada:
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    option = int(input('Digite o número referente a opção: '))
    if option == 1:
        soma = n1 + n2
        print('O valor da soma dos dois números {} + {} é: {}'.format(n1, n2, soma))
    elif option == 2:
        multi = n1 * n2
        print('O valor multiplicado de {} x {} é: {}'.format(n1, n2, multi))
    elif option == 3:
        if n1 > n2:
            print('O número {} é maior que {}'.format(n1, n2))
        if n2 > n1:
            print('O número {} é maior que {}'.format(n2, n1))
    elif option == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite mais um número: '))
    elif option == 5:
        print('Finalizando o programa...')
    else:
        print('Opção inválida. Tente novamente!')
print('Fim do programa! Volte sempre....')
