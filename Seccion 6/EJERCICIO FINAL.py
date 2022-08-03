'''
Uno de los métodos más famosos para calcular el número pi (π), por su facilidad de implementación, es la igualdad matemática conocida como Serie de Leibniz. Esta se apoya en varias propiedades matemáticas para determinar
el valor de π al realizar una sumatoria infinita de números definidos en un patrón sencillo. Aunque en la práctica no es posible considerar realizar infinitas operaciones,
aún se puede lograr cierta aproximación, ya que conforme mayor sea el número de valores empleados en la sumatoria, más cerca estará el resultado obtenido del valor de pi (π).'''

### Los codigos son copiados del curso de la Universidad Nacional de Colombia

### ESCRIBA SU CÓDIGO A PARTIR DE AQUÍ ### (~ 7-10 líneas de código)

# Entrada del programa (~ 1 línea).
n = int(input())

# Serie de Leibniz (~ 5-8 líneas).
pi = 0
signo = 1
for i in range(1,n,2):
    pi = pi + signo * (1/i)
    signo = -signo
pi = pi*4
# Salida del programa con 10 decimales (~ 1 línea).
print(f"{pi:.10f}")