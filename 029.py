
print('Limite de velocidade: 80km/h')
m = int(input('Qual a velocidade do seu carro?:'))
if m>80 :
    print('Você está {}km acima do limite permitido e foi multado em {} R$.' .format((m-80),(m-80)*7))
else :
    print('Limite permitido')