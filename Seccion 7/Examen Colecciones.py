
Canciones = {}

while True:
    comando = input()

    if comando == 'añadir':

        cancion = input()
        artista = input()

        if artista not in Canciones:
            Canciones[artista] = list()
        Canciones[artista].append(cancion)

    elif comando == 'reproducir':

        artista = input()

        if artista in Canciones:

            if len(Canciones[artista]) > 0:
                cancion = Canciones[artista].pop(0)
                print(f'Reproduciendo {cancion} de {artista}.')
                Canciones[artista].append(cancion)
            else:
                print('No quedan canciones en cola.')
        else:
            print('El artista no tiene canciones registradas.')
    elif comando == 'listar':
        artista = input()
        if artista in Canciones:
                listado = Canciones[artista]
                for posicion, cancion in enumerate(listado):
                    print(f'{posicion+1}. {cancion}')
        else:
            print("El artista no tiene canciones registradas.")
    elif comando == 'detener':
        print('Terminando la sesión. ¡Hasta pronto!')
        break

    else:
        print('Comando no reconocido. Intente de nuevo:')