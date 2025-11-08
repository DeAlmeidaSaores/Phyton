import math
a = float(input('DIgite o ângulo que você deseja:'))
s = math.sin(math.radians(a))
print('O ângulo {} tem seno = {}'.format(a,s))
print('O ângulo {} tem cosseno = {}'.format(a, math.cos(math.radians(a))))
