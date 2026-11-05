from datetime import date
atual = date.today().year
ano = int(input('Digite sua seu ano de nascimento: '))
idade = atual - ano
print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, atual))
if idade == 18:
    print('Voçê deve se alistar IMEDIATAMENTE')
elif idade < 18:
    saldo = 18 - idade
    print('Voçê não pode se alistar pois não tem 18 anos. Ainda faltam {} anos para o seu alistamento'.format(saldo))
    dev = atual + saldo
    print('Seu alistamento será em {}'.format(dev))
elif idade > 18:
    saldo = idade - 18
    print('Voçê deveria ter se alistado a {} anos'.format(saldo))
    dev = ano -saldo
    print('Seu alistamento deveria ter sido em {}'.format(dev))