q = ' '
l = []
while q not in 'Nn':
    m = int(input('Digite um valor:'))
    q = str(input('Quer continuar?'))
    l.append(m)
l.sort(reverse=True)
print(f'Você digitou {len(l)} elementos.')
print(f'Os valores em ordem decrescente são {l}')
if 5 not in l:
    print('Tem o valor 5')
else:
    print('Tem o valor 5')




