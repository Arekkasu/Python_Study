Old = int(input('Ingresa tu edad: '))
Etapa = None

#Forma tradicional
'''if Old >= 0 and Old  < 11:
    print('Infancia')
elif Old >= 10 and Old < 21:
    print('Comienza el Estudio')
elif Old >=20 and Old <= 30:
    print('El amor y el trabajo empieza')
else:
    print('Etapa no identificada') '''

#Simplificada
if 0 <= Old  < 10:
    Etapa = 'Infancia'
elif 11 <= Old  < 20:
    Etapa = 'Comienza el Estudio'
elif 21 <= Old  == 30:
    Etapa = 'El amor y el trabajo empieza'
else:
    print('Etapa no identificada')

print(f'Tu edad es : {Old}, y estas en la etapa {Etapa}')