# 12 Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Valor do produto: R$ '))
desc = preco - (preco * 5 / 100)
print(f'O valor do produto com desconto de 5% será: R$ {desc}')
