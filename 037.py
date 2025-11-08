me = int(input('Digite um número:'))
print('Em qual base você quer converter esse número?')
print('\033[35m''-=''\033[m'*20)
print(' Digite: \n 1 para binário \n 2 para octal \n 3 para hexadecimal')
print('\033[35m''=-''\033[m'*20)
n = int(input('Vamos lá:'))
if n == 1 :
    print('{} convertido para binário é igual a{}:'.format(me, bin(me)[2:]))
elif n  == 2:
    print('{} convertido para octal é igual a:{}'.format(me, oct(me)[2:]))
elif n == 3:
    print('{} convertido para hexadecimal é igual a:{}'.format(me, oct(me)[2:]))
else:
    print('opção inválida')