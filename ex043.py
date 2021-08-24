from time import sleep
nome = str(input('Qual o seu nome? '))
sleep(1)
print('~'*10)
print('Olá \033[1;35m{}\033[m, seja bem-vindo(a) a calculadora de índice de Massa Corporal'.format(nome))
print('~'*10)
sleep(1)
peso = float(input('Me diga qual o seu peso? Kg: '))
altura = float(input('Qual a sua altura?: '))
print(" \033[36mAnalisando o seu IMC...\033[m ")
sleep(3)
imc = peso / (altura ** 2)
print('Seu IMC é de {:.2f}, sua classificação é'.format(imc), end='')
if imc <= 18.5:
    print('\033[35m Abaixo do seu peso \033[m')
elif imc > 18.5 and imc < 25:
    print('\033[35m Peso ideal \033[m')
elif imc > 25 and imc < 30:
    print('\033[35m Sobrepeso \033[m')
elif imc > 30 and imc < 40:
    print('\033[35m Obesidade \033[m')
else:
    print('\033[35m Obesidade Mórbida \033[m')