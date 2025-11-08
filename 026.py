frase = str(input('Digite uma frase:')).strip()
print('A letra A aparece {} vezes'.format( frase.upper().count("A")))
print('Ela aparece na posição \033[4m{} \033[31mpela primeira vez'.format(frase.upper().find('A')+1))
print('ELa aparece pela última vez na posição {}.'.format(frase.upper().rfind('A')+1))