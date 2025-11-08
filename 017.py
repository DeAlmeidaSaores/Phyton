from math import sqrt, hypot

m = float(input('Qual a medida do cateto posto do seu triângulo?'))
n = float(input('Agora diga-me qual a medida do cateto adjacente:'))
a = sqrt(m) + sqrt(n)
# pode ser também (hypot(co, ca))
print('O comprimento da hipotenusa é: {}'.format(sqrt(a)))
