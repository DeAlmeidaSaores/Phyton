from traceback import print_tb

tu = ( 'Zero,', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis',
      'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis',
      'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
print(f'Lista de times:{tu}')
print(f'Os 5 primeiros sao {tu[0:5]}')
print(f'OS 4 ultimos sao {tu[-4:]}')
print(f'Em ordem alfabética é {sorted(tu)}')
print(f'o cinco ta na {tu.index("Cinco")+1} posição')