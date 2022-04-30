#Rango de los 20's y 30's
Edad = int(input('Ingresa tu edad: '))
Ran_20 = Edad >= 20 and Edad < 30
print(Ran_20)
Ran_30 = Edad >= 30 and Edad < 40
print(Ran_30)
if Ran_20 or Ran_30:
    print('Estas en el rango de los 20\'s y los 30\'s')
else:
    print('No estas en el rango')
