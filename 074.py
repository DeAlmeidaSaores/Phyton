from random import randint
n = (randint(0,10),randint(0,10),randint(0,10),
     randint(0,10),randint(0,10))
print('Os valores sorteados foram:')
for c in n:
    print( c, end=' ')
print('\n',f'o maior foi {max(n)}')
print(f' o menor foi {min(n)}')