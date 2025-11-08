print('Posso te falar se um ano é bissexto ou não')
m = int(input('Diga qual ano você quer saber:'))
if m %  4 == 0 and m % 100 != 0 or m % 400 == 0 :
    print('Bissexto')
else:
    print('Não é bissexto')
