maior = 0
menor = 0
valores = []
for c in range(0,5):
    valores.append(int(input('Digite um número:')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor :
            menor = valores[c] #valor da lista no laço na rodada equivalente
print(f'O maior valor digitado foi {maior} na posição ', end='')
for c, i in enumerate(valores):
    if i == maior:
        print(c)
print(f'O menor valor digitado foi {menor} na posição ', end='')
for c, i in  enumerate(valores):
    if i == menor:
        print(c)

print(f'Voce digitou {valores}')



