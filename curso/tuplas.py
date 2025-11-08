lanche = ('pizza', 'arroz', 'vatapa')
for c in range(0, len(lanche)):
    print(f'comi {lanche[c]} na posição {c}') #a variavel lanche e o contador indicam cada elemento no tupla e depois so o contador indica a posiçao
    #ouuuuuuu
for c in lanche: #se nao precisa das posicao
 #ooooooooouuuuuuuuuu
    print(f' comi {c}')
for pos, comida in enumerate(lanche): # posicao e palavra
    print(f'comi {comida} na posicao {pos}')
#definamos uma tupla t = ('pao', 'arroz')
# t[1] nos mostra arroz
#sorted(lanche) mostra em ordem alfabética
def soma(a, b):
    s = a + b
    print(s)


soma(3,5)