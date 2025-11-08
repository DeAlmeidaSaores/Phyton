c = ('\033[m',
     '\033[0;97;41m', # 1 - vermelho
     '\033[0;97;42m', # 2 - verde
     '\033[0;97;43m', # 3 - amarelo
     '\033[0;97;44m', # 4 - azul
     '\033[0;97;45m', # 5 - roxo
     '\033[7;97m')   # 6 branco
def texto(z, cor = 0):
    print(c[cor], end='')
    print('~'*(len(z)+4))
    print(f'  {z}')
    print('~' * (len(z) + 4))
    print(c[0], end='')
def t():
    from time import  sleep
    sleep(0.8)
    print('.', end='')
    sleep(0.8)
    print('.', end='')
    sleep(0.8)
    print('.')
    sleep(0.8)
def fun():
    l = str(input('Função ou Biblioteca > '))
    print(c[1],end='')
    texto(f'Acessando o manual do comando {l}',4)
    print(c[0], end='')
    t()
    while True:
        if l:
            print(c[6], end='')
            help(l)
            print(c[0], end=' ')
            l = str(input('Função ou Biblioteca > '))
        if l in 'fim':
            texto('Até logo', 1)
            break


#Progama pincipal
texto('SISTEMA DE AJUDA PyHELP', 1)
fun()
