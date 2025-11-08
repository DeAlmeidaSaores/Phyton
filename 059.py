from time import sleep
m = int(input('Digite um número:'))
n = int(input('Digite outro número:'))
v = 0
while not v== 5:
    print('   [ 1 ]Somar\n   [ 2 ]Multiplicar\n   [ 3 ]Maior\n   [ 4 ]Novos números\n   [ 5 ]Saior do programa')
    v = int(input('O que você quer fazer:'))
    if v == 1 :
        print('A soma entre {} e {} é: {}'.format(m,n,(m+n)))
    elif v == 2:
        print('A multiplicação entre {} e {} é: {}'.format(m,n,(m*n)))
    elif v == 3:
        if m > n:
            print('O maior número entre {} e {} é: {}'.format(m,n,m))
        elif m < n:
            print('O maior número entre {} e {} é: {}'.format(m,n,n))
        else:
            print('São iguais. Vamos denovo:')
    elif v == 4:
        print('Informe seus números novamente:')
        m = int(input('Digite um número:'))
        n = int(input('Digite outro número:'))
    elif  v == 5:
        print('Finalizando...')
        sleep(2)
    else:
        print('Opção inválida. Tente novamente:')
print('=-='*10)
print('Fim')


