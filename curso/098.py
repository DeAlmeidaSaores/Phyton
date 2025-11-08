from time import sleep
def contador(i , f , p):
    if p < 0:
        p *= - 1
    if p == 0:
        p = 1
    print('-='*20)
    print(f'Contador de {i} até {f} de {p} em {p}.')
    sleep(2)
    cont = i
    if i < f:
        while cont <= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont += p
        print('FIM')

    else:
        while cont >= f:
            print(f'{cont}' , end=' ')
            sleep(0.5)
            cont -= p
    print('FIM')


#Progama princípal
contador(1 ,10, 1)
contador(10,1,1)
print('~~~AGORA É SUA VEZ~~')
print('=-'*10)
a = int(input('Início: '))
b = int(input('Fim:    '))
c = int(input('Passo:  '))
contador(a, b, c)

def contador( a, b, c):
    f = a
    while a <= f:
        print(f'{f}')
        f += c


contador(1,10,1 )