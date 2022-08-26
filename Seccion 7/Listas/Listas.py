'''Las listas son mutables (SE PUEDEN MODIFICAR, LAS LISTAS TIENEN UN INICIO Y UN FINAL
HACIENDO QUE LAS LISTAS SEAN SECUENCIALES'''

from contextvars import copy_context
from tokenize import Number


lista = list(range(0,20,2))
print(lista)

#Indices - se refiere a la ID de un elemento de la lista o coleccion de datos

n = len(lista)  #Saber cuantos elementos tiene
print(n)

#al recorrer una conjunto de datos se inicia de 0 hasta el final, no  de 1 en 1

for i in range(n):
	print(f'el elemento {lista[i]} tiene como ID a {i}')  #los '[]' es para referencia el ID



# Index a la inversa

if lista[-1] == lista[n-1]:
	print(f'list[-1]:\t{list[-1]}\t list[n-1]:\t {list[n-1]}')

print(lista[5:0:-1])

#matriz

Matriz = [[0,1,2],	#lista con ID[0],
		  [3,4,5],
		  [6,7,8],	#LISTAS CON ID[2]
				]
print(Matriz[2][1])

#Operar con listas

lista_2 = list(range(11))

print(lista_2[::2])  #salta de 2 en 2
print(lista_2 + list('hola')) #Agrega 'Hola'
print(lista*3) #triplica

#Listas Methods

	#Agregar elemento
lista.append(575)
print(lista)

lista.insert(7,16) #primer numero 7  es el index y 11 el elemento que se agregara
print(lista)

	#remover
lista.remove(16)
print(lista)

	#saber la id de un elemento (solo puede devolver uno)
print(lista.index(575))
	#por ID
lista.pop(10)

#listas por compresion es ahorrar lineas en una iteracion

num = list(range(1,9))

li = []

for x in num:
	if x < 5:
		li.append(x**2)

print(li)

#con compresion

l2 = [x**2 for x in num if x < 5]
print(l2)

#Referencias y apuntadores
"""En esto se refiere a como las variables tienen su refetencia o como son apuntadas en la
memoria del Dispositivo"""

a = 'hola'
b = 'hola'

#aqui dara True debido a que los STR son inmutables y tiene su propia direccion de memoria

#Se refiere si el objeto de las variables son el mismo de la memoria
print(a is b)

#Referencias y apuntadores en listas

print("""El usar 'IS' no dara True, debido a que la lista si pueden obtener igual de elemento pero son distintos en la
ubicacion de la memoria""")

A = [1, 2, 3, 4]
B = [1, 2, 3, 4]

#Dara False
print(A is B)

#Dara True
print(A == B)

#como Hacer que compartan el mismo Objeto

#Ahora haremos esto

C = A

print(A is C)

print('Vamos a mirar el ID 1 de las listas C y A')
print()
print(A[1])
print(C[1])
print(A[1] == C[1])

#Si hago una modificacion en C o en A, afectara a toda aqueva variable que sea el mismo objeto de este

C[1] = 'Se modifico'

print(f'A[1]: {A[1]}')
print(f'C[1]: {C[1]}')

#Hacer una copia de una lista sin ser afectada la original

#copy()

D = A.copy()

print(f'metodo D.copy() {D}')

#ejemplo mas elaborado

Numbers = [1, 2, 3]
Copy_Numbers = Numbers[:] # --> copia de Numbers

Numbers[0] = 'Se'
Numbers[1] = 'Cambio'

print(Numbers)

print(Copy_Numbers)


print('La modificacion')
print()
print(Numbers is Copy_Numbers) # --> Falso debido a que es una copia y tiene su propia ubicacion en la memoria
print()
print(f'como queda la lista Numbers --> {Numbers}')
print()
print(f'Como queda la copia --> {Copy_Numbers}')


#Listas de Listas
print('-----------')
print()
print('Copia de listas')
Matriz_1 = [
	list(range(4)),
	list(range(4,9)),
	list(range(8,13))
]

copy_b = Matriz_1

copy_c = Matriz_1[:]

print(Matriz_1)
print()
print(copy_b)
print()
print(copy_c)
print()

print('-------Modificaciones---------')

print()

print(Matriz_1)
copy_b[1] = 10
print()
print(copy_b)
print()
print(f'{copy_c} --> No se agrega el 10')

print('----------------------------')
copy_c[0] = 11

print(f'{Matriz_1}')
print()
print(f'{copy_b}')
print()
print(f'{copy_c} --> Se modifica ahora si')

print('----------------------------')
print()
copy_c[2][1] = '200'
print(f'{Matriz_1} --> se modifica')
print()
print(f'{copy_b} --> se modifica')
print()
print(f'{copy_c} --> se modifica')
