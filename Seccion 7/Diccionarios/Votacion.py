
num_entradas = int(input())

# diccionario de candidatos
candidatos = {}

for nombre in range(num_entradas):
    nombre = str(input())
    if nombre in candidatos:
        candidatos[nombre] += 1
    else:
        candidatos[nombre] = 1

# Obtener los votos e ir sumando según corresponda (~ 3-5 líneas)
ganador = max(candidatos.values())
empate = 0

for i in candidatos:
    if(ganador==candidatos[i]):
        empate+=1
        if(empate>1):
            break
if empate>1:
    print("EMPATE")
else:  
    print(max(candidatos, key=candidatos.get))
# Definir resultado (~ 3-6 líneas)

# Salida del programa (~ 1 línea).
