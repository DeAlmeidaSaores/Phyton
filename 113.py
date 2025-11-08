def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Erro!! Digite um número inteiro válido.')
            continue
        except (KeyboardInterrupt):
            print('O usuário preferiu não digitar!')
            return 0
        else:
            return n

def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('Erro!! Digite um número inteiro válido.')
            continue
        except (KeyboardInterrupt):
            print('O usuário preferiu não digitar!')
            return 0
        else:
            return n


n1 = leiaint('Digite um número inteiro:')
n2 = leiafloat('Digite um número real:')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')
