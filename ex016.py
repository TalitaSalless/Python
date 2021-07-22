# Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Digite um numero: 6.127. O numero 6.127 tema a parte inteira 6.
from math import trunc
n = float(input("Digite um numero: "))
int = trunc(n)
print ("O valor digitado foi {} e a sua porção inteira é {}".format (n,int))