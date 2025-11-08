from datetime import date
atual = date.today().year
cont = 0
for c in range(1,8):
    m = int(input('Digite o ano de nascimento da {}º pessoa:'.format(c)))
    v = atual - m
    if v >= 21:
        cont +=1
print('{} pessoas têm idade superior a 21 anos'.format(cont))
print('{} pessoas ainda não atingiram  a maioridade'.format(7 - cont))