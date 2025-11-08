def fatorial(n, show=False):
    """""
    -> Calcula o fatorial de um número.
        - n recebe o valor.
        - se show == True a função devolve o valor pro print
        mas não amazena em nehum lugar, por isso não há necessidade
        de pedir print dentro da função.
        - show sempre será False, a não ser que seja pedido.
    """""
    d = 1 #aqui simplesmente eu defino d
    for c in range(n, 0, -1):
        d *= c
        if show: #aqui o python entende que if show é if show == True
            print(f'{c}', end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
    return d #aqui já retorna o valor quando chamo a função





print(fatorial(10, True))
help(fatorial)