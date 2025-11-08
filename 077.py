l = ('Laranja',
     'Banana',
     'Pera',
     'Uva',
     'Maça')
for c in l:
    print(f'\nNa palavra {c.upper()} temos', end=' ')
    for b in c:
        if b in 'aeio U':
            print(b.upper(), end=' ')