def leiaInt(a):
    m = str(input(a))
    while True:
        if m.isnumeric():
            m = int(m)
            break
        else:
            print('\033[0;31mErro!!\033[m')
            m = str(input(a))
    return m



n = leiaInt('Digite um número:')
print(f'Você acabou de digitar o número {n}.')
