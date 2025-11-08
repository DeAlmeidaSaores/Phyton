l = ('Lápis', 1.75,
     'Borracha', 2,
    'Caderno', 15,
    'Estojo', 12,
    'Mochila', 30,
    'Caneta', 5)
for pos in  range( 0, len(l)):
    if pos % 2 == 0:
        print(f'{l[pos]:-<30}', end='')
    else:
        print(f'R${l[pos]:.>2.2f}')
