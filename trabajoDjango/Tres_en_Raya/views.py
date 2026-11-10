from django.shortcuts import render

def tres_en_raya(request):

    if request.method == 'POST':

        tablero = request.POST.get('tablero')
        turno = request.POST.get('turno')
        posicion = int(request.POST.get('posicion'))

        # Convertimos el tablero en una lista
        tablero = list(tablero)

        # Comprobamos que la casilla esté vacía
        if tablero[posicion] == '-':

            # Colocamos la ficha del jugador
            tablero[posicion] = turno

            # Volvemos a convertir el tablero en string
            tablero = ''.join(tablero)

            # Combinaciones posibles para ganar
            combinaciones = [
                (0, 1, 2),
                (3, 4, 5),
                (6, 7, 8),
                (0, 3, 6),
                (1, 4, 7),
                (2, 5, 8),
                (0, 4, 8),
                (2, 4, 6)
            ]

            # Comprobamos si alguien ha ganado
            ganador = False

            for a, b, c in combinaciones:
                if tablero[a] == tablero[b] == tablero[c] and tablero[a] != '-':
                    ganador = True

            if ganador:
                mensaje = '¡Ha ganado el jugador ' + turno + '!'
                terminado = True

            elif '-' not in tablero:
                mensaje = '¡Empate! No quedan casillas libres.'
                terminado = True

            else:
                # Cambiamos el turno del jugador
                if turno == 'X':
                    turno = 'O'
                else:
                    turno = 'X'

                mensaje = 'Turno de ' + turno
                terminado = False

        else:
            # Si la casilla está ocupada, no cambiamos el turno
            tablero = ''.join(tablero)
            mensaje = 'Esa casilla ya está ocupada. Turno de ' + turno
            terminado = False

    else:
        # Valores iniciales del juego
        tablero = '---------'
        turno = 'X'
        mensaje = 'Turno de X'
        terminado = False

    contexto = {
        'tablero': tablero,
        'turno': turno,
        'mensaje': mensaje,
        'terminado': terminado,
    }

    return render(request, 'TresEnRaya.html', contexto)
