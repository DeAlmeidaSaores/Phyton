from time import sleep
from random import randint
print('Suas opções')
print(' [ 0 ] PEDRA \n [ 1 ] PAPEL \n [ 2 ] TESOURA')
m = int(input('Qual é a sua jogada?'))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
print('-='*20)
sorte = ('PEDRA', 'PAPEL', 'TESOURA')
pc = randint(0,2)
print('O computador escolheu {}.'.format(sorte[pc]))
if m == pc:
    print('EMPATE!')
elif m == 0 and pc == 1:
    print('VoCÊ PERDEU!')
elif m == 0 and pc == 2:
    print('VOCÊ GANHOU!')
elif m == 1 and pc == 0:
    print('VOCÊ GANHOU!')
elif m == 1 and pc == 2:
    print('VOCÊ PERDEU!')
elif m == 2 and pc == 0:
    print('VOCÊ PERDER!')
elif m == 2 and pc == 1:
    print('VOCÊ GANHOU!')
else:
    print('JOGADA INVÁLIDA!')
print('-=' * 20)
