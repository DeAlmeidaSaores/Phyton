a1 = int(input('Digite um valor:'))
r = int(input('Digite a razão:'))
dec = a1 + (10 - 1) * r #calculando o 10º termo da PA
for c in range(a1, dec, r):
    print(c, end='-> ')
print('Fim')