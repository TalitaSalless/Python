co = float(input('Comprimento o cateto oposto:'))
ca = float(input('Comprimento de cateto adjacente:'))
hi = (co ** 2 + ca ** 2) ** (1/2)
print ('A hipotenusa vai medir {:.2f}'.format(hi))

#com importação MATH:
from math import hypot
co = float(input('Comprimento o cateto oposto:'))
ca = float(input('Comprimento de cateto adjacente:'))
hi = hypot(co, ca)
print ('A hipotenusa vai medir {:.2f}'.format(hi))
