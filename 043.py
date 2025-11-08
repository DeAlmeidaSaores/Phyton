m = float(input('Digite o seu peso:'))
n = float(input('Digite sua altura:'))
v = n * (m**2)/2
print(v)
if v < 18.5:
    print('Abaixo do peso!!!')
elif v > 18.5 and v <26:
    print('Peso ideal')
elif v > 24 and v >31:
    print('Sobrepeso')
elif v > 29 and v < 41:
    print('Obesidade')
elif v > 40:
    print('Obesidade mórbida')