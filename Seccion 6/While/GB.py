'''

Se ha decidido realizar una copia de seguridad de todos los archivos de una empresa pequeña. Para esto, se necesita adquirir un nuevo disco duro que pueda almacenar toda esa información. Se quiere gastar lo mínimo posible, por lo que se plantea comprar el dispositivo que tenga la capacidad mínima necesaria para realizar el respaldo.

Inicialmente, identifica que toda la información que se desea almacenar tiene un tamaño total w (en Giga Bytes o GB), y que en el proveedor de tecnología con el que se va a adquirir el disco duro solo vende unidades con capacidades determinadas en potencias de 2

, disponibles desde 1 GB.

En este ejercicio deberá realizar un programa que reciba el tamaño en GB de los archivos que se desean almacenar e imprima en pantalla la capacidad necesaria en GB del dispositivo de almacenamiento.

'''
tamano = float(input())

#informacion que desea almacenear
w = 0
#capacidad para almacenar
capacidad = 2**w #se pone el 2 primero ya que w es en potencia de 2, es decir 2 se eleva a w

while capacidad<tamano:
    capacidad = 2**w
    w += 1

print(f'necesita un disco de {capacidad} GB')