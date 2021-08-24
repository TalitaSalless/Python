valor = float(input('Digite o valor do produto: R$ '))
print('''OPÇÕES DE PAGAMENTO:
[1] A VISTA dinheiro/cheque: 10% de desconto
[2] A VISTA cartão: 5% de desconto
[3] Cartão até 2x: preço normal 
[4] Cartão 3x ou mais : com 20% de juros ''')
opcao = int(input('Qual a opção desejada? '))
if opcao == 1:
    total = valor - (valor * 10 / 100)
elif opcao == 2:
    total = valor - (valor * 5 / 100)
elif opcao == 3:
    total = valor
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opcao == 4:
    total = valor + (valor * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcela em {}x de R$ {:.2f} COM JUROS'.format(totparc, parcela))
else:
    total = valor
    print('Opção inválida de pagamento. Tente novamente!')
print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final'.format(valor, total))
