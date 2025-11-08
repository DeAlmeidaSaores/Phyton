soma = 0
cont = 0
m = 0
n = ' '
maior = 0
menor = 0
while n not  in 'Nn':
    m = int(input('Digite um número:'))
    n = str(input('Quer continuar?')).strip().upper()
    soma += m
    cont += 1
    if cont == 1:
        maior = menor = m #no contador ==1 que eu criei eu salvo o primeiro valor nas duas variaveis manor e maio. depois disso o contador == 1 nao é mais ultilizadp
    else: #depois, todos vem direto pro else
        if m > maior: #depois de renderizar pela segunda vez eu posso ter uma possibilidade de comparação com a variavel m que ja foi digitada pela segunda vez com a variavel maior que eu salvei quando o contador estava em 1
            maior = m
        if m < menor: #os if sao avaliados um após o outro
            manor = m
v = soma/cont
print('Você digitou {} número e a média entre eles foi {}'.format(cont, v))
print(f'O menor é {menor} e o maior é {maior}')