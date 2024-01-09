import funciones_wumpus as f

while True:
    #Variables:
    print()
    n = input('Ingrese dimensión del tablero: ')
    while True:
        if n.isdigit():
            n = int(n)
            if n >= 4:
                break
        print()
        n = input('\033[91m' + 'Valor inválido. ' + '\033[0m' + 'Ingrese un' + '\033[91m' + ' NÚMERO ' + '\033[0m' + 'mayor o igual a 4: ')

    print()
    pits = input('Ingrese número de hoyos: ')
    while True:
        if pits.isdigit():
            pits = int(pits)
            if pits >= 1 and pits <= n - 1:
                break
        print()
        pits = input('\033[91m' + 'Valor inválido. ' + '\033[0m' + 'Ingrese número VÁLIDO de hoyos: ')

    print()

    wumpus = input('Ingrese número de wumpus: ')
    while True:
        if wumpus.isdigit():
            wumpus = int(wumpus)
            if wumpus >= 1 and wumpus <= n - 1:
                break
        print()
        wumpus = input('\033[91m' + 'Valor inválido. '+ '\033[0m' + 'Ingrese número VÁLIDO de wumpus: ')

    #crear tablero:
    tablero = f.crearTablero(n)
    f.crearWumpus(tablero, n, wumpus)
    f.positionStench(tablero, n)
    f.crearPits(tablero, n, pits)
    f.positionBreeze(tablero, n)
    f.crearGold(tablero, n)

    #variables
    y = n - 1
    x = 0
    jugadas = 0
    breik = False
    orito = False

    while True:
        f.imprimir(tablero)
        #f.imprimido(tablero) #función para ver la matriz

        movimiento = str(input("")).upper()

        x, y, jugadas = f.moverse(movimiento, x, y, jugadas, tablero, n)
        breik, orito = f.verificarposiciones(breik, orito, tablero, x, y)
        if breik == True:
            f.imprimir(tablero)
            print(f"Jugadas totales: {jugadas}.".center(75))
            break

    print()
    print('-'.center(75, '-'))
    print()
    print('¿Quieres jugar otra vez?'.center(75))
    print()
    otra = input("Si quiere volver a jugar, ingrese SÍ: ")
    print()
    if str(otra).upper() in ["SI", "SÍ"]: continue
    else:
        print("¡Gracias por jugar WUMPUS! Esperamos que te haya gustado.".center(75))
        print()
        print('\033[1m' + "CRÉDITOS".center(75))
        print('\033[94m' + "Samanta Chang".center(75))
        print("Fiorella Falcón".center(75))
        print("Delia Juy".center(75))
        print()
        print('\033[0m' + ' FIN DEL JUEGO '.center(75, '-'))
        break
