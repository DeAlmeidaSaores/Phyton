def ficha(a='', b=''):
    if a == '':
        a = '<Desconhecido>'
    if b.isnumeric():
        b = int(b)
    else:
        b = 0
    print(f'O jogador {a} fez {b} gol(s)no campeonato.')



print('--'*20)
m = str(input('Nome do jogador:')).strip()
j = str(input('Número de Gols:'))
ficha(m,j)