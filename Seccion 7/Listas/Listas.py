'''Las listas son mutables (SE PUEDEN MODIFICAR, LAS LISTAS TIENEN UN INICIO Y UN FINAL
HACIENDO QUE LAS LISTAS SEAN SECUENCIALES'''

list = list(range(1,20,3))
print(list)

#Indices - se refiere a la ID de un elemento de la lista o coleccion de datos

n = len(list)  #Saber cuantos elementos tiene
print(n)

#al recorrer una conjunto de datos se inicia de 0 hasta el final, no  de 1 en 1

for i in range(n):
	print(f'el elemento {list[i]} tiene como ID a {i}')  #los '[]' es para referencia el ID



# Index a la inversa

if list[-1] == list[n-1]:
	print(f'list[-1]:\t{list[-1]}\t list[n-1]:\t {list[n-1]}')

print(list[5:0:-2])