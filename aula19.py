estado = dict()
brasil = list()
for c in range(0,2):
    estado['uf'] = str(input('Unidade federativa:'))
    estado['sigla'] = str(input('Sigla do estado:'))
    brasil.append(estado.copy()) # o copy eh necessário pq em todo loop é sobrescrito o valor se nao salvar
for e in brasil:
    print(f'{e["uf"]} fica em {e["sigla"]}')