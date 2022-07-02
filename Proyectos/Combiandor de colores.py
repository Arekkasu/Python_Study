Color_1 = str(input('Ingrese el color 1 : '))
Color_2 = str(input('Ingrese el color 2: '))
Combinacion = ''
if Color_1 == 'Rojo' and Color_2 == 'Azul':
    Combinacion = 'Morado'
elif Color_1 == 'Azul' and Color_2 == 'Rojo':
    Combinacion = 'Morado'
elif Color_1 == 'Amarillo' and Color_2 == 'Rojo':
    Combinacion = 'Naranja'
elif Color_1 == 'Rojo' and Color_2 == 'Amarillo':
    Combinacion = 'Naranja'
elif Color_1 == 'Azul' and Color_2 == 'Amarillo':
    Combinacion = 'Verde'
elif Color_1 == 'Azul' and Color_2 == 'Amarillo':
    Combinacion = 'Verde'
else:
    print('error')

print(f'{Combinacion}')


