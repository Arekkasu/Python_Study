print('Desempaquetado de Tuplas'.center(100,'-'))

print()

print('Son la base de una poderosa funcion de asignacion de tuplas\nque permite qasignacion de multiples valores en una sola declaracion')

print()

print('Ejemplo:\nEn este ejemplo se hara que el apellido sea dividido con la declaracion de una sola variable')

print()

nombre,apellido = str('Alexander Lozada').split()

print()

print(f'{nombre}\n{apellido}')

print()

print('Multiple declaracion en 1 linea')

tupla = 1,2,3 #--> Recuerda que no es obligatorio los parentesis en una tupla

a,b,c = tupla

print(tupla)
print()
print(a,b,c)

print()

print('intercambio de valor')

print()

a,b = 10, 20

print(f'a = {a}\nb = {b}')

a, b = b, a

print()

print(f'ahora vale asi\n\na = {a}\nb = {b}')

print()

print('QUE PUEDO HACER SI HAY VALORES QUE SOBREPASAN LA CANTIDAD DE VARIABLES?')

print()

print('Para hacer esto hay que agregar una variable demas de lo que pides con un \'*\'')

print()

print('Ejemplo: \n')

a,b,*c = 1, 2, 3, 4 ,5, 6

print(f'a tendra como valor a {a}\nb tendra como a {b}\ny c tendra como valores los siguientes = {c} y los guarda en una lista')

print('Iteracion sobre coleccion de Tuplas'.center(100,'-'))

print()

print('Las siguientes funciones son importantes que retornan colecciones de tuplas usadas para creear iterables especiales')

print()

(print('1. Enumerate(iterable): Tiene como funcion regresar el Indes y el valor de algun iterable y lo regresa en forma de tupla\n'))

print('''
for tupla in enumerate(tupla_ejemplo):
    print(tupla)\n ''')

tupla_ejemplo = 1, 2, 3 ,4

for tupla in enumerate(tupla_ejemplo):
    print(tupla)

tupla_ejemplo = 1, 2, 3 ,4

print()

print('Para no recibir en formato tupla en su estructura se debe poner 2 valores en este caso pondre Index y valor')

print()

print('''
for index, valor in enumerate(tupla_ejemplo):
    print({index+1} {valor})\n Recuerda que en los recorridos empieza desde 0 y no en 1''')

for index, valor in enumerate(tupla_ejemplo):
    print(f'{valor+1}. {index}')

print()

print('2. Zip(iterable): Permite tomar 2 o mas iterables como argumentos y emparejar sus varoles\nEs util para realizar operaciones enrte los varoles de dos colecciones, o para unir los valores a un tabla')

A = (1, 2, 3) 

B = (4, 5, 6)

C = (7, 8, 9)

print()

for a,b,c in zip(A, B, C):
    print(f'{a} {b} {c}')

print()

print(f'Aqui se crearon 3 tuplas, A = {A} B = {B} Y C = {C}, y con zip hicimos que se combinaran los valores')

print()

print('Con enumare y zip a la vez quedaria algo asi')

print()

print('   A B C')
print()

for indice, (a,b,c) in enumerate(zip(A, B, C)):
    print(f'{indice}. {a} {b} {c}')