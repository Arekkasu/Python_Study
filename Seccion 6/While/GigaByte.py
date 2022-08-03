### ESCRIBA SU CÓDIGO A PARTIR DE AQUÍ ### (~ 5 líneas de código)

# Entrada del programa (~ 1 línea).
tamaño = float(input())                       # Reemplace 'None' por el código necesario.
w = 0
capacidad = 2**w
# Cálculo de la capacidad (~ 3 líneas).
while capacidad<tamaño:
    capacidad = 2**w
    w += 1

# Salida del programa (~ 1 línea).
print(f'La capacidad requerida es de {capacidad} GB.')