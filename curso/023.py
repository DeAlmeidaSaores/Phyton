num = int(input('Digite um numero de 0 á 9999:'))
v = num // 1 % 100
b = num // 10 % 10
m = num // 100 % 10
g = num // 1000 % 10
print('unidade: {}'.format(v))
print('Dezena: {}'.format(b))
print('Centena: {}'.format(m))
print('Milhar: {}'.format(g))


