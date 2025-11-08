ficha = list()
q =' '
while q not in 'nN':
    nome = str(input('Nome:'))
    nota1 = float(input('Nota 1:'))
    nota2 = float(input('Nota 2:'))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    q = str(input('Quer cotinuar?'))
print('-='*15)
print(f'{"No":<4}{"NOME":<10}{"MÉDIA":>8}')
print('--'*15)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8}')
print('--'*15)
while True:
    l = int(input('Mostrar quais notas?'))
    if l == 999:
        print('ACABOU')
        break
    if l <= len(ficha)-1:
        print(f'A nota de {ficha[l][0]} são {ficha[l][1]}')





