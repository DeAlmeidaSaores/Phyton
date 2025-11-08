soma = 0
cont = 0
for c in range(1, 7):
    m = int(input('Digite o {}º valor:'.format(c)))
    if m % 2 == 0:
        soma += m
        cont += 1
print('você informou {} números pares e a soma deles foi {}.'.format(cont, soma ))


