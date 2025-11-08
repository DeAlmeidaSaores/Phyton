m = (int(input('Digite o numero:')),
     int(input('Digite o numero:')),
     int(input('Digite o numero:')),
     int(input('Digite o numero:')),
     int(input('Digite o numero:')))
print(m)
print(f'o valor 9 apareceu {m.count(9)} vezes')
if 3 in m:
    print(f'O valor 3 apareceu na {m.index(3)+1} posição')
else:
    print('O valor 3 não foi digitado em nehuma posição')
print('os valores pares encontrados foram:', end=' ')
for n in m: # n é a variável e guarda o valor de cada loop e m é a sequência que o for percorre
    if n % 2 == 0:
        print(n, end=' ')