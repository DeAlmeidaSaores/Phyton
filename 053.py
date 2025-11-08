m = str(input('Digite uma frase:')).strip().upper()
p = m.split()
n = ''.join(p)
inv = ''
for etra in range(len(n) - 1 , -1 , -1):
    inv += n[etra]
if inv == n :
    print(n, inv)
else:
    print(n, inv)


