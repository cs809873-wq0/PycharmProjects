print('{:=^40}'.format(' LOJAS CHZIM '))
preço = float(input('Preço das compras R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinhairo/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input(' Qual é a opção: '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f} COM JUROS'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R$ {:.2f}'.format(totparc, parcela))
print('Sua compra de {}R$ vai custar {}R$ no final.'.format(preço, total))
