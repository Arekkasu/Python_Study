Numero = int(input('Ingresa un numero del 1 al 3: '))
#Esta variable obtendra un valor despues de ser usada en la funcion
numeroTexto = ''

if Numero == 1:
    numeroTexto = 'Uno'
elif Numero == 2:
    numeroTexto = 'Dos'
elif Numero == 3:
    numeroTexto = 'Tres'
else:
    print(f'El numero {Numero} esta fuera del rango')

print(f'El numero que ingresaste ({Numero}) en escrito es {numeroTexto}')