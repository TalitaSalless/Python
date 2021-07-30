casa = float(input('Qual o valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento?'))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print("Para pagar uma casa de \033[32m R${:.2f}\033[m em \033[33m{} anos\033[m".format(casa, anos), end='')
print(" a prestação será de \033[31mR${:.2f}".format(prestacao))
if prestacao <= minimo:
    print('Emprestimo pode ser concedido!')
else:
    print('O emprestimo será negado!')