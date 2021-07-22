#08 Escreva um programa que leia um valor em metro e o exiba convertido em centímetros e milímetros.
medida = float(input('Digite quantos metros;'))
cm = medida * 100
mm = medida * 1000
print (f' A média de {medida} corresponde a {cm:.0f}cm e {mm:.0f}mm')
