usuario_correto = 'eu12345'.strip().upper()
senha_correta = '12345678'.strip().upper()
usuario = str(input('Digite seu USUÁRIO: '))
senha = str(input('Digite sua SENHA: ')).strip().upper()
while senha and usuario not in 'usuario_correto''senha_correta':
    usuario = str(input('USUÁRIO INVÁLIDO. Tente Novamente: '))
    senha = str(input('SENHA INCORRETA. Tente Novamente: '))
print('SEJA BEM VINDO')

