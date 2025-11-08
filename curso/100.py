from random import randint
from time import sleep


def sorteio(lista): #Lá dentro da função, o parâmetro lista aponta para o mesmo lugar na memória que numeros
    cont = 0
    while cont <= 4 :
        k = randint(0,10)
        if k not in lista:
            lista.append(k)
            cont += 1
            print(f'{k}', end=' ')
            sleep(0.4)
def somaPar(lista):
    p = 0
    for c in lista:
        if c % 2 == 0 :
            p += c
    print(f'Na lista: {lista} temos soma de números pares igual a {p}')



numeros = list() #passo 1 criar uma lista
sorteio(numeros) #passa essa lista como argumento pra funçao
somaPar(numeros) #aqui eu acesso a lista ja criada na primeira função
#IMPORTANTE: lista é so um argumento e so tem valor dentro da função
#A ligação se da através de numeros e nao de lista
