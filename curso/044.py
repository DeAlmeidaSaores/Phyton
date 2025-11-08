m = int(input('Digite o preço do seu produto:'))
print('Entendi...')
n = int(input('Digite: \n 1 - Para pagamento á vista. \n 2 - Para pagamento á vista no cartão. \n 3 - Para pagamento em até 2x no cartão. \n 4 - Para pagamento em 3x ou mais no cartão.\n'))
if n == 1:
    print('Seu produto á vista ficará por R${}.'.format( m-(m*10/100)))
elif n == 2:
    print('Seu produto á vista no cartão ficará por R${}.'.format(m-(m*5/100)))
elif n == 3:
    print('Seu produto em 2x no cartão ficará por R${}.'.format(m))
elif n == 4:
    print('Seu produto em 3x ou mais ficará por R${}.'.format((m*20/100)+ m))
