m = int(input('Digite o valor do seu salário para saber o aumento:'))
if m>1250:
    aumento = (m*10)/100
else:
    aumento = (m*15)/100
print('Seu novo salário é {:.2f}R$'.format(aumento + m))