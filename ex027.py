nome = str(input('Digite o seu nome completo:')).strip().upper()
separa = nome.split()
print('Seu primeiro nome é: {}'.format(separa[0]))
print('O seu ultimo nome é: {}'.format(separa[-1]))
