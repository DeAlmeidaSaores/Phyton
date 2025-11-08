from time import sleep
m = int(input('Diga-me quantos anos você tem: '))
print('Entendi...\nAgora vamos ver qual categria você pertence:')
sleep(1)
if m < 10:
    print('MIRIM')
elif m > 9 and m < 15:
    print('INFANTIL')
elif m > 14 and m < 20:
    print('JUNIOR')
elif m > 19 and m < 21:
    print('SÊNIOR')
else:
    print('MASTER')
