temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome:')))
    temp.append(int(input('Peso:')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
             mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    q = str(input('Quer continuar?'))
    if q in 'Nn':
        break
print(f'Voce cadastrou {len(princ)} pessoas')
print(f'O mair peso foi {mai}kg de', end=' ')
for c in princ:
    if c[1] == mai:
        print(f'{c[0]}')
print(f'O menor peso foi {men}kg de ', end=' ')
for c in princ:
    if c[1] == men:
        print(f'{c[0]}')

