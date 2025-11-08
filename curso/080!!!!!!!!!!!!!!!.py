lista = []
for c in range(0, 5):
    n = int(input('Digite um número:'))
    if c == 0 : #aqui adiciona o primeiro ou último, dependendo o elif
        lista.append(n)
        print(f'Adicionado ao final da lista.')
    elif n > lista[-1]: #se for maior que o último valor da lista
        lista.append(n) #caso seja menor que c==0 pula-se pro else
        print(f'Adicionado ao final da lista.') #até aqui o código adiciona o  último elemento
    else:
        pos = 0
        while pos < len(lista): #vai de 0 ao ultimo índice da lista
            if n <= lista[pos]:#lista na posição #pega o elemento da lista na posição pos, seja pos 0, 1....
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista.')
                break
            pos += 1
print(f'Os valores digitados em ordem foram {lista}')