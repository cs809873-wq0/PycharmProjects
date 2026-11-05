import time
distancia = float(input('Qual a distância da sua viajem? '))
print('Voçê está prestes a começar uma viajem de {}Km'.format(distancia))
print('PROCESSANDO...')
time.sleep(2)
if  distancia <= 200:
    preço = distancia * 0.50
    print('O preço da sua viajem de {}Km sairá no valor de R${:.2f}'.format(distancia, preço))
else:
    preço = distancia * 0.45
    print('Sua viajem de {}Km sairá no valor de R${:.2f}'.format(distancia, preço))
