m = 0
cont = 0
soma = 0
m =  int(input('Digite um valor:'))
while m != 999:
     cont += 1
     soma += m
     m = int(input('Digite um valor:'))
print('fim com {} termos com soma = {}'.format(cont, soma))

