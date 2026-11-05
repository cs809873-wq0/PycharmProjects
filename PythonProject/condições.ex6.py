from datetime import date
ano = int(input('Que ano quer saber? Coloque 0 para saber sobre o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Esse ano {} é BISSEXTO'.format(ano))
else:
    print('Esse ano {} não é \033[7;4mBISSEXTO\033[m'.format(ano))