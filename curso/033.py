m = int(input('Digite um número:'))
n = int(input('Digite outro número:'))
o = int(input('Digite o último número:'))
cores = {'limpa': '\033[31m',
          'azul': '\033[34m', }
if m > n and m> o:
    maior = m
if  n > m and n > o:
    maior = n
if o > m  and o > n :
    maior = o
if m < n and m < n :
    menor = m
if n < o and n < m :
    menor = n
if o < m and o < n :
    menor = o
print('o menor número é: {}{}'.format(cores['limpa'],menor))
print('O maior número é: {}{}'.format(cores['azul'],maior))
