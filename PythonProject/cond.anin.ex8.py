peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Voçê está ABAIXO do peso \033[2;32mNORMAL\033[m')
elif 18.5 <= imc < 25:
    print('Voçê está no peso \033[2;32mIDEAL\033[m')
elif 25 <= imc < 30:
    print('Voçê está com \033[2;33mSOBREPESO\033[m')
elif 30 <= imc < 40:
    print('Voçê está com \033[2;31mOBESIDADE\033[m')
else:
    print('Voçê está com \033[2;31mOBESIDADE MÓRBIDA\033[m, cuidado!')