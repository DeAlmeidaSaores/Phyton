primeiro = int(input('Digite o priemiro termo da PA:'))
razao = int(input('Digite a razão da PA:'))
termo = primeiro
cont = 1
while cont <= 10:
   print('{}'.format(termo), end=' ')
   cont +=1
   termo += razao
print('Fim')