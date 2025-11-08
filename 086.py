matriz = [[0,0,0],[0,0,0],[0,0,0]]
somador = d = maior = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Dgitie um valor para {(l), (c)}:'))
        if matriz[l][c] % 2 == 0:
            somador += matriz[l][c]
for l in range(0,3):
        for c in range(0,3):
            print(f'[{matriz[l][c]:^5}]', end='')
        print()
        if c == 2:
            d += matriz[l][c]
        if matriz[1][0]:
            maior =  matriz[1][0]
        if matriz[1][1] > maior:
            maior = matriz[1][1]
        if matriz[1][2] > maior:
            maior = matriz[1][2]
print(f'A somar de todos os valores pares é {somador}:')
print(f'O valor dos valores da terceira coluna é {d}:')
print(f'O maior valor da segunda linha foi {maior}:')
o 86 e 87 foram juntos

