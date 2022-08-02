fila = 1

while fila <= 10:
    columna = 1
    linea = ''
    while columna <= 10:
        linea += f'{fila * columna}\t'
        columna = columna+1
    
    print(linea)
    fila = fila+1