def area(l, c): # l e c são parâmetros formais
    s = l * c
    print(f'A área de um terreno {l}x{c} é de {s}m².')



#Progama princípal
print('Controle de Terrenos')
print('--'*10)
a = int(input('LARGURA (m):'))
b = int(input('COMPRIMENTO (m):'))
area(a, b)  #aqui eu chamo a função e dou valores para l e c


