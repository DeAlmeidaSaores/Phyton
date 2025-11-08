import random
m = str(input('Digite o nome do primeiro sortudo:'))
n = str(input('Agora vamos ao segundo:'))
o = str(input('Será que esse terá mais sorte:'))
p = str(input('Dizem que os últimos serão os primeiros, certo?!'))
l = [m,m,o,p]
c = random.choice(l)
print('Muito bem, {}, talvez você atá possa jogar na megasena, já que dessa você apagará o quadro!Good loocky in the nex chance'.format((c)))