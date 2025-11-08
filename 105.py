def notas(*n, situ = False):
    """
     - Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos.
    :param situ: valor opcional indicando se deve adicionar a situação.
    :return:dicionário com as várias informações.
    """
    z = dict()
    mai = men = cont = med = 0
    for c, j in enumerate(n):
        if cont == 0:
            mai = men = j
        if j > mai:
            mai = j
        if j < men :
            men = j
        med += j
        cont += 1
    z['Média'] = med/cont
    z['Total'] = cont
    z['Menor'] = men
    z['Maior'] = mai
    if med >= 6 and situ:
        z['Situação'] = 'Boa'
    if med < 6 and situ:
        z['Situação'] = 'Ruim'
    return z


#Progama principal
resp = notas(5.5, 9.5, 10, 6.5, situ = True) #aqui eu tenho que chama situ,
# pq o pyhton não tem como perceber se True é nota ou Situ já que usei desempacotamento
print(resp)