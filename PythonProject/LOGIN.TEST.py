usuario_correto = 'ursula021'
senha_correta =  'Coxinha2122'
usuario = input('Digite seu usuário: ')
senha = input('Digite sua senha: ')
if usuario == usuario_correto and senha == senha_correta:
    print('\033[2;32mACESSO LIBERADO\033[m. Aproveite sua navegação!')
else:
    print('\033[2;31mACESSO NEGADO\033[m. Tente novamente')


