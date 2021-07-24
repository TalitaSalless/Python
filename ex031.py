distancia = int(input('Qual a distancia da viagem em Km?: '))
print('Voce está prestes a começar uma viagem de {}Km.'.format(distancia))
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('O preço da sua passagem será: R${:.2f}'.format(preco))