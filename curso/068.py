from random import randint
print('=-='*20)
print('VAMOS JOAGAR PAR OU ÍMPAR')
print('=-='*20)
cont = 0
while True:
    m = int(input('Diga uma valor:'))
    n = randint(0,10)
    c = str(input('O que você quer? [P/I]')).upper().strip()[0]
    if c in 'Pp' and (m + n) % 2 == 0 or (c in 'Ii' and (m + n) % 2 != 0):
        cont += 1
        print(f'Você digitou {m} e computador digitou {n}. Você ganhou.')
    else:
        print(f'Você digitou {m} e o computaodr digitou {n}. Você perdeu')
        break
    print(f'E jogou {cont} vezes')

