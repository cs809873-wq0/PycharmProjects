casa = float(input('Qual o valor da casa que voçê deseja comprar? R$'))
salario = float(input('Qual o valor do seu salário? R$'))
anos = int(input('Por quantos anos deseja pagar a casa? '))
prestaçao = casa / (anos * 12)
minimo = salario * 30 / 100
print('\nPara comprar uma casa de R${:.2f} em {} anos'.format(casa, anos))
print('\nA prestação será de R${:.2f}'.format(prestaçao))
if prestaçao <= minimo:
    print('\nEmpréstimo pode ser CONCEDIDO')
elif prestaçao >= minimo:
    print('\nEmpréstimo NEGADO')
