i = [[], []]
for c in range(1, 6):
    m = int((input(f'Digite o {c}º valor:')))
    if m % 2 == 0:
        i[0].append(m)
    else:
        i[1].append(m)
print(f'OS valores pares digitados foram {sorted(i[0])}')
print(f'OS valores pares digitados foram {sorted(i[1])}')



