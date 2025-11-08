from random import randint
from time import sleep
l = []
j = []
print(f'*'*30)
print(f'      Joga na Mega Sena')
print(f'*'*30)
m = int(input(f'Quantos jogos você quer que sorteie?'))
tot =1
while tot <= m:
    cont = 0
    while True:
        a = randint(0,60)
        if a not in l:
            l.append(a)
            cont +=1
        if cont >= 6:
            break
    l.sort()
    j.append(l[:])
    l.clear()
    tot +=1
print('=-'*7, f'Criando {m} jogos','=-'*7)
sleep(0.4)
for c, i in enumerate(j):
    print(f'Jogo {c+1}: {i}')
    sleep(0.6)
print(f'-='*10, f'BOA SORTE', f'-='*10)

