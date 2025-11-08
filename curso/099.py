from time import sleep
def maior(* numero):
    m = c = 0
    print('Analisando os valores...')
    for j, k in enumerate(numero):
        print(f'{k}', end=' ')
        sleep(0.3)
        if j == 0:
            m = k
        if k > m:
            m = k
        c += 1
    print(f'Foram informados {c} valores ao todo.\nO maior valor foi {m}.')


#Progama princpal
maior(1,2,3,4,9)
maior(4)
maior()
maior(19, 9)