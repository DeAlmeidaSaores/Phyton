q = ' '
l = []
v = []
t= []
while q not in 'Nn':
    m = int(input('Digite um número:'))
    q = str(input('quer continuar?'))
    v.append(m)
    if m % 2 == 0:
        l.append(m)
    else:
        t.append(m)
print(f'A lista completa é {v}')
print(f'A lista de pares é {l}')
print(f'A lista de ímpares é {t}')
