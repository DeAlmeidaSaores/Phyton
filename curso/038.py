from time import sleep
print('\33[32m''-''\33[m' *25)
n = int(input('Digite o primeiro número:'))
print('\33[32m''-''\33[m' *25)
print('\33[37m''Gostei do número''\33[m')
sleep(1)
m = int(input('Agora digita outro número:'))
print('\33[37m''Processando...' '\033[m')
sleep(1)
if n > m :
    print('o primeiro valor é maior')
elif m > n :
    print('O segundo valor é maior')
else:
    print('Não existe maior, os dois são iguais')

