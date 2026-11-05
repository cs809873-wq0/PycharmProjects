n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print('Quem tirou {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, media))
if media <= 5 or media < 7:
    print('O aluno está de RECUPERAÇÃO')
elif media < 5:
    print('Aluno REPROVADO')
else:
    print('Aluno APROVADO')

