n = int(input('Digite o numero:'))
print('Calculando {}! = '.format(n), end=' ')
f = 1
c = n #Pra não perder o valor original, caso precise usar.
while c > 0:
    print('{}'.format(c), end=' ')
    print('x' if c > 1 else '=', end=' ')
    f *=c
    c -= 1
print('{}'.format(f))