frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))
for letra in range(-1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um PALÍDROMO')
else:
    print('Não temos um PALÍDROMO')
