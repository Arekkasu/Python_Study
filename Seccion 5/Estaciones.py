Mes = int(input('Ingresa el numero del mes para saber que estacion es: '))
Estacion = ''

if Mes >=3 and Mes <=6:
    Estacion = 'Primavera'
if Mes >=7 and Mes <=9:
    Estacion = 'Verano'
if Mes >=10 and Mes <=12:
    Estacion = 'Otono'
if Mes == 1 or Mes == 2:
    Estacion = 'Invierno'
else:
    print(f'Ingresa bien el valor')
print(f'{Estacion}')