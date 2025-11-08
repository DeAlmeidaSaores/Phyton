l = list()
d = dict()
cont = 0
d['nome'] = str(input('Nome do jogador:'))
p = int(input(f'Quantas partidas {d['nome']} jogou:'))
for c in range(1, p+1):
    b = int(input(f'Quantas gols na partida {c}:'))
    l.append(b)
    cont += b
d['gols'] = l
d['total'] = cont
print(f'-='*20)
print(d)
print(f'-='*20)
for k, c in d.items():
    print(f'O campo {k} tem valor {c}.')
print(f'-='*20)
print(f'O jogador {d['nome']} jogou {p} partidas.')
for q, w in enumerate(l):
    print(f'=> Na partida {q+1}, fez {w} gols.')
