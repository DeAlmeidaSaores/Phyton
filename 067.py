m = int(input('Você quer ver a tabuada de que valor?'))
cont = 1
while cont <= 10:
    cont += 1
    if m < 0:
        break
    print(f'{m} X {cont} = {m * cont}')
    if cont == 10:
        cont = 0
        m = int(input('Você quer ver a tabuada de que valor?'))
