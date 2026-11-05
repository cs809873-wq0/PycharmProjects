s = float(input('Informe o salário do funcionario R$: '))
if s <= 1250:
    novo = s + (s * 15 / 100)
else:
    novo = s + (s * 10 / 100)
print('Quem recebia R${} de salário, agora passará a receber R${}'.format(s,novo))
