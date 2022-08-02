Usr = float(input('Proporciona el valor (0 a 10): '))
Note = None

if 9 <= Usr == 10:
    Note = 'A'
elif 8 <= Usr < 9:
    Note = 'B'
elif 7 <= Usr < 8:
    Note = 'C'
elif 6 <= Usr < 7:
    Note = 'D'
elif 0 <= Usr < 6:
    Note = 'F'
else:
    print('Valor incorrecto')

print(f'{Note}')