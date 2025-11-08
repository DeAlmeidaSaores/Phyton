m = (float(input('Digite a distância da sua viagem:')))
if m<=200 :
    preco = m*0.45
else:
    preco = m*0.5
print('Sua corrida custará {}R$'.format(preco))