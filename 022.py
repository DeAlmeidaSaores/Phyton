n = str(input('Digite seu nome completo:')).strip()
print('Seu nome em maiúculo é: {} '.format(n.upper()))
print('Seu nome em minúsculo é: {}'.format(n.lower()))
print('Seu nome ao todo tem {} letras'.format(len(n) - n.count(' ')))

#print('O primeiro nome tem {} letras'.format(n.find(' ')))
v = n.split()
#print('Seu primeiro nome é: {} e ele tem {} letrinhas'.format(v[0], len(v[0])))
print(v)