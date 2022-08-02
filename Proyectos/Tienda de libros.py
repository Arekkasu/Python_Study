#Tienda dE libros
print('Pproporcione los siguientes datos: ')
#inputs
Name = str(input('Proporciona el nombre: '))
ID = int(input('Proporcion el ID: '))
Price = float(input('Ingresa el Precio'))
Envio = str(input('Indica si el envio es gratiuto (True/False): '))

if Envio == 'True':
    Envio = True
elif Envio == 'False':
    Envio == False
else:
    Envio = 'Incorrecto, Ingresa (True/False)'
#-----
print(Name)
print()
print(ID)
print()
print(Price)
print()
print(Envio)