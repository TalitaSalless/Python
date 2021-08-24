print('-.'*20)
print('Média da sala! :)')
print('-.'*20)
n1 = float(input('Nota do aluno 1: '))
n2 = float(input('Nota do aluno 2: '))
media = (n1 + n2) / 2
print('Tirando {} e {}, a média do aluno é {}'.format(n1,n2,media))
if 7 > media >= 5:
    print('O aluno(a) está de recuperação!')
elif media < 5:
    print('O aluno(a) está reprovado(a)!')
elif media >= 7:
    print('O aluno(a) está aprovado(a)!')