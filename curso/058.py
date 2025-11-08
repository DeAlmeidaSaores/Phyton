from random import randint
cont=1
print('Vamos testar sua sorte hoje!\nQual o número estou pensando?\nDe 0 a 10')
m = int(input('Diga:'))
c = randint(0,5)
while not c == m:
    m = int(input('Ainda não acertou!!\nTente novamente:'))
    cont += 1
print('Boa!!!! Você tentou {} vezes até conseguir!'.format(cont))