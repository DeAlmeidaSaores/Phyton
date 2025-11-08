def voto(a):
    from datetime import date
    k = date.today().year
    b = k - a
    if 16 <= b < 18 or b > 65:
        return f'Opicional'
    elif b < 16:
        return f'Negado'
    else:
        return f'Obrigatório'

m = int(input('Digite o ano do seu nascimento:'))
print(voto(m))