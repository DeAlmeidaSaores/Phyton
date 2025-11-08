a = int(input('Digite o valor do primeiro segmento de reta:'))
b = int(input('Digite o valor do segundo segmento de reta:'))
c = int(input('Digite o valor do terceiro segmento de reta:'))
if a + b > c and b + c > a and a + c > b:
    print('Sim, você conseguirá formar um triângulo')
else:
    print('Não conseguirá forma um triângulo!')
