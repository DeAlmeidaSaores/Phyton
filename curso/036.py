from time import sleep
print('\033[34m''=-''\033[m' *20)
print('\033[35m''Bom dia, vamos começar!''\033[m')
print('\033[34m''=-''\033[m' *20)
m = float(input('Primeiro, diga-me o valor do imóvel que desejas comprar:'))
print('Analisando...')
sleep(1)
print('Ok... É um ótimo preço:')
renda = float(input('Agora, me informa a sua renda:'))
print('Entendi...')
sleep(1)
o = int(input('E em quantos anos o senhor pretende quitar o imóvel?'))
print('Verficando uma útlima vez...')
sleep(2)
ano = o*24
prestacao = m / ano
if prestacao <= renda*30/100 :
    print('Aprovado')
else:
    print('Sua renda é incompatível!!!')
