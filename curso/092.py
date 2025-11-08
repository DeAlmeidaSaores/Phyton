from datetime import datetime
d = dict()
d['Nome'] = str(input('Digite seu nome:'))
p = int(input('Digite seu ano de nascimento:'))
z = datetime.now()
d['Ano'] = z.year - p
m = int(input('Carteira de trabalho (0 não tem):'))
if m != 0:
    d['CTPS'] =  m
    d['Contratação'] = int(input('Ano de contratação:'))
    d['Salario'] = int(input('Salário R$:'))
    d['Aposentario'] = d['Ano'] + 35
    print(f'-='*20)
for l, k in d.items():
    print(f'- O {l} é {k}.')




