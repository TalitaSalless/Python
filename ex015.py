dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados?' ))
pago = (60 * dias) + (km * 0.15)
print('O total a pagar é de {:.2f}'.format(pago))
