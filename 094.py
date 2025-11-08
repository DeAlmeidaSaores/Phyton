galera = list()
pessoa = dict()
somador = cont = 0
while True:
    pessoa['nome'] = str(input('Nome:'))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print(f'Digite M ou F.')
    pessoa['idade'] = int(input('Idade:'))
    somador += pessoa['idade']
    cont += 1
    galera.append(pessoa.copy())
    pessoa.clear()
    while True:
        resp = str(input('Quer continuar?')).upper()[0]
        if resp in 'SN':
            break
        print('Digite Sim ou Não!!!')
    if resp == 'N':
        break
print(f'-='*20)
print(f'Foram cadastradas {len(galera)} pessoas.')
print(f'A média de idade foi {somador/cont:5.2f}. ')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'As mulheres cadastradas forma {p["nome"]}.' , end=' ')
print()
print('Lista de pessoas que estão acima da média:')
for p in galera:
    if p['idade'] >= somador/cont:
     print('       ', end='')
     for k, v in  p.items():
         print(f'{k} = {v};')
     print()
print('<< ENCERRADO >>')


