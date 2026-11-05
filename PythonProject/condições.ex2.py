from random import randint
import time
computador = randint(0 , 5)# Faz o computador pensar
jogador = int(input('Em que número estou penando? '))
print('PROCESSANDO...')
time.sleep(1)
print('-=-'*10)
if jogador == computador:
    print('Voçê VENCEU!!!!!')
else:
    print('Voçê PERDEU o número que eu pensei foi o {} e não o {}'.format(computador, jogador))
