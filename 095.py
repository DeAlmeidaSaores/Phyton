l = list()
d = dict()
t = list()
cont = 0
tot = 0
while True:
    l.clear()
    d.clear()
    tot = 0
    d['nome'] = str(input('Nome do jogador:'))
    d['partidas'] = int(input(f'  Quantas partidas {d['nome']} jogou:'))
    for c in range(1, d['partidas']+1):
        k = (int(input(f'  Quantos gols na partida {c}:')))
        tot += k
        l.append(k)
    d['gols'] = l.copy()
    d['total'] = tot
    t.append(d.copy())
    m = str(input('Quer continuar?'))
    if m in 'Nn':
        print(t)
        break
print()
print(f'-='*20)
print(f'{"Nome":<10} {"Gols":^5} {"Total":>20}')
print('-'*40)
for v, k in enumerate(t):
     print(f"{k['nome']:<10} {str(k['gols']):^5} {k['total']:>15}")
print(f'-='*20)
while True:
    x = int(input('Mostrar dados de qual jogador?'))
    k = x - 1
    if k == 998:
        break
    if k == 0:
        print('Erro')
    if k >= len(t): #como a lista começa de 0 pode ser >= que sempre será um número a menos do que a lista mostra
        print(f'Erro!!! Digite um número de 1 a {len(t)}')
    else:
        print(f'--LEVANTAMENTO DO JOGADOR  {t[k]["nome"]}:')
        for i, g in enumerate(t[k]['gols']):
            print(f'    NO jogo {i+1} fez {g} gols.')
    print(f'--'*10)
print(f'    --VOLTE SEMPRE--')














