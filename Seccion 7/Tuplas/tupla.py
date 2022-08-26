print('Tuplas'.center(100, "-"))

print()

#Que es una tupla

print('Es una secuencia de elementos de cualquier tipo\nsolo qye con la caracteristica que es inmutable\n(No se puede modificar su valor o es unico)')

#creacion
print()

print('las tuplas se pueden crear de la siguiente manera:\n\n\t1. tupla = 1, 2 ,6 ,3 ,6\n\t2. tupla = (1, 2 ,3 ,6)')

print()

print('Para establecer una tupla vacia es asi --> t = ()\ny al usar type() dara como salida tuple')

print()

print('Para una tupla de un elemento se debe hacer de la forma siguiente\nt = (\'tupla\',) importante la coma')

print()

print('-'.center(99,'-'))

print()

print('Las tuplas pueden usarse en los ciclos\n')

tupla_ejemplo = (1, 2, 3, 5, 4, 6)

print(f'Hice esta tupla con los siguientes valores {tupla_ejemplo}\nhara un ciclo for imprimiendo sus elementos')

print()

for i in tupla_ejemplo:
    print(i)

print()

print('Modificacion de tupla'.center(100,"-"))

print()

print('Que las tuplas sean inmutables, no significa que no puedan se puedan reasignar como una tupla nueva.')

print()

print('''lista = [7, 8]

tupla_ejemplo = tupla_ejemplo+tuple(lista)\n''')

lista = [7, 8]

tupla_ejemplo = tupla_ejemplo+tuple(lista)                                                                                                                                      

print(tupla_ejemplo)

print()

print('Pero nunca se puede reasignar un valor dentro de la tupla es decir si el elemento con ID \'0\' y le cambiamo su valor a X, dara error')
