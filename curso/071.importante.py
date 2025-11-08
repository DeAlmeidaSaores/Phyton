print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Qual valor você quer sacar?'))
total = valor
ced = 50
tot = 0
while True:
    if total >= ced:
        total -= ced
        tot  += 1
    else:
        if tot > 0 :
            print(f'Foram {tot} cédelas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        tot = 0
        if ced == 0:
            break
