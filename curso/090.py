doc = dict()
doc['Nome'] = str(input('Digite seu nome:'))
doc['Media'] = float(input(f'Digite a média de {doc["nome"]}: '))
if doc['media'] >= 6:
    doc['situ'] = 'Aprovado'
elif 5 <= doc['media'] < 7:
    doc['situação'] = 'Recuperação'
else:
    doc['Situação'] = 'Reprovado'
for d, k in doc.items():
    print(f'{d} é {k}')

