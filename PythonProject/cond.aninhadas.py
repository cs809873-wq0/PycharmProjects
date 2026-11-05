nome = str(input('qual é seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Paulo' or nome == 'Joana' or nome == 'Pedro':
    print('Nossa seu nome é bem popular no Brasil!')
elif nome in 'Ana Cláudia Jéssica Beatriz':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia {}'.format(nome))
