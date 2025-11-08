print('-'*25)
print('   LOJA    ')
print('-'*25)
cont = 0
dont = 0
baratu = 0
barato = ' '
num = 0
while True:
    n = str(input('Nome do produto:'))
    p = int(input('Preço:'))
    num +=1
    cont += p
    if p > 1000:
        dont += 1
    if num == 1:
        baratu = p
        barato = p
    else:
        if p < baratu:
            baratu = p
            barato = p
    print('-' * 25)
    q = ' '
    while q not in 'SN':
        q = str(input('Quer continuar?')).upper().strip()[0]
    if q == 'N':
        print('----------FIM DO PROGRAMA---------')
        print(f'O total da comproa foi R${cont}')
        print(f'Temos {dont} produtos custando mais de R$1000.00')
        print(f'O produto mais barato {barato} e custou R${baratu}')
        break
