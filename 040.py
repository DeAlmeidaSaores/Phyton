m = float(input('Digite a sua primeira nota:'))
n = float(input('Digite a sua segunda nota:'))
o = (m+n)/2
print(o)
if o < 5:
    print('Reprovado')
elif (o > 5) and o < 6.9 :
    print('Recuperação')
else:
    print('Aprovado')