import random
m = str(input('Digite o primeiro nome:'))
n = str(input('Digite o segundo name:'))
o = str(input('Tell me about the thirth:'))
p = str(input('Agora o último gay:'))
l = [m,n,o,p]
random.shuffle(l)
print('A ordem das abeçãdos é: {}'.format(l))