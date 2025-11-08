from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogador1': randint(1,6),
        'Jogador2': randint(1,6),
        'Jogador3': randint(1,6),
        'Jogador4': randint(1,6)}
ranking = list()
print(f'Os valores sorteados:')
for k, v in jogo.items():
    print(f'O {k} tirou {v}')
    sleep(0.5)
print(f'-='*20)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) # o jogo.items me permite percorrer os valores do dicionario sem tranformar ele em tupla
for p, q in enumerate(ranking):
    print(f'O {q[0]} ficou em  {p+1}º e tirou {q[1]}')
    sleep(1)