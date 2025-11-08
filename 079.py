q =  ' '
l = []
while q not in 'Nn':
    m = int(input('Digite um valor:'))
    if m not in l:
        l.append(m)
    else:
        print('Valor duplicado e não adicionado.')
    q = str(input('Quer continuar?'))
l.sort()
print(f'Sua lista ficou assim : {l}')
