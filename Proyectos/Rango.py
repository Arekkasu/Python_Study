#Detecto de tango de X numero
value = int(input('Ingrese el valor: '))
if value >= 0 and value <= 5:
    print(f'{value} Esta en el rango')
else:
    print(f'{value} No esta en el rango')
print()
print()
print()
print('Otra forma')

range_number = (value >= 0 and value <= 5)
if range_number:
    print(f'{value} esta en el rango')
else:
    print(f'{value} no esta en el rango')