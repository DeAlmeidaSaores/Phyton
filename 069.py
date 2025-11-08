contu = 0
cont = 0
homem = 0
mulher20 = 0
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    i = int(input('Idade:'))
    s = ' '
    while s not in 'MF':
        s = str(input('Sexo:')).upper().strip()[0]
    if i > 18:
        cont += 1
    if s == 'H':
        homem +=1
    if s == 'M':
        if i < 20:
            mulher20 += 1
    contu +=1
    print('-' * 20)
    q = ' '
    while q not in 'SN':
        q = str(input('Quer continuar?')).upper().strip()[0]
    if q == 'N':
        print(f'{cont} pessoas tem mais de 18 anos.')
        print(f'Foram cadastrados {contu} pessoas')
        print(f'{mulher20} tem menos de 20 anos')
        break