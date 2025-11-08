from datetime import date
dat = date.today().year
m = int(input('Diga-me qual ano você nasceu, caso ainda não tenha realizado o alistamento obrigatório:'))
print('Excelente')
n = ( dat - m)
if m == 18:
    print('Você já possui 18 anos. AListe-se já!!!')
elif n < 18:
    print('Você possui {} anos. Faltam {} anos para seu alistamento'. format(n, (18 - n)))
else:
    print('Você está em débito com o país. Procure a junta de alistamento mais próxima.')