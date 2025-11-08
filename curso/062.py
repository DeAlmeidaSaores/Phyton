primeiro = int(input('Digite o primeiro termo de uma PA:'))
razao = int(input('Digite a razão da PA:'))
termo = primeiro
cont = 1
mais = 10
total = 0
while mais != 0: #continua enquanto n digitar 0 na var mais
    total = total + mais #atualiza o total de termos a ser mostrado com a var mais
    while cont <= total : #conta ate o total de termos pedido na var mais
        print('{}'.format(termo), end=' ') #mostra o priemeiro termo
        cont += 1 #conta pra encerrar na var total
        termo += razao #pula o termo somando á razao
    mais = int(input('\nQuanto termos você quer que eu mostre?')) #após encerrado o laço pede mais repetições
print('fim com {} termo'.format(total))