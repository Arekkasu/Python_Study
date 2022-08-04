'''Las listas son mutables (SE PUEDEN MODIFICAR, LAS LISTAS TIENEN UN INICIO Y UN FINAL
HACIENDO QUE LAS LISTAS SEAN SECUENCIALES'''

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