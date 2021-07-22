# 13 Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Salário do funcionário: R$ '))
aumento = salario + (salario * 15 / 100)
print(f'O salário do funcionário com aumento de 15% será R$ {aumento} reais.')
