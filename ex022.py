#Crie um programa que leia o nome completo de uma pessoa e mostre:#O nome com todas as letras maiusculas;
#O nome com todas as minusculas;#Quantas letras aotodo sem considerar espaços;#Quantas letras temm o primeiro nome;

nome = str(input("Digite seu nome completo:")).strip()
print("Analisando o seu nome...")
print("Seu nome em maiúsculas é {}".format(nome.upper()))
print("Seu nome em minúsculas é {}".format(nome.lower()))
print("Seu nome tem ao todo {} letras".format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))


