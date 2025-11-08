tu = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    m = int(input('Digite um número de 0 a 20: xxxxx'))
    while  0 < m > 20:
        m = int(input('Digite um número de 0 a 20 aaaaaaa:'))
    print(f'Você digitou o número {tu[m]}')
    n = str(input('Você quer continuar xxxxxx?')).strip().upper()
    if n in 'Nn':
        break









