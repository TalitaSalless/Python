n = int(input('Digite um numero: '))
print('Analisando o numero {}...'.format(n))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('A unidade dele é: {}'.format(u))
print('A dezena dele é: {}'.format(d))
print('A centena dele é: {}'.format(c))
print('O milhar dele é: {}'.format(m))
