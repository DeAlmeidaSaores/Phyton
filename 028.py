from random import randint
from time import sleep
print('Ok... Vou pensar um número de 0 a 5 e você tenta acertar, certo?')
m = input('OK... Me diz qual você acha que foi:')
print('Será???????')
sleep(2)
n = randint(0,5)
if m == n:
 print('boa')
else:
 print('Se lascou')
 print('foi {}'.format(n))