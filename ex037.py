num= int(input("Digite um número inteiro: "))
print('''Escolha uma das opções abaixo: 
[1] converter para bínário
[2] converter para octal
[3] converter para hexadecimal''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('O numero {} em binário será {}'.format(num, bin(num)[2:]))#usar o fatiamento
elif opcao == 2:
    print('O número {} em octal será {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('O número {} em hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('Opção INVÁLIDA. Tente novamente!')
