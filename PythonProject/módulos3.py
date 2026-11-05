import math
an = float(input('Digite o ângulo que voçê deseja:'))
seno = math.sin(math.radians(an))
print('O ângulo {} tem o SENO de {:.2f}'.format(an, seno))
cosseno =math.cos(math.radians(an))
print('O ângulo {} tem o COSSENO de {:.2f}'.format(an, cosseno))
tangente = math.tan(math.radians(an))
print('O ângulo {} tem a TANGENTE de {:.2f}'.format(an, tangente))

