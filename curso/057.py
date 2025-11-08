m = str(input('Digite o seu sexo [M/F]:')).strip().upper()
while m not in 'MmFf':
    str(input('Dados invalidos. Digite novamente:')).strip().upper()
print('Sexo {} registrado com sucesso!'.format(m))