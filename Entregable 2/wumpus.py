import funciones_wumpus as f
import json

# FUNCIÓN DEL JUEGO
def juego(tablero, y, x, jugadas, breik, orito, n, flecha):
    while True:
        f.imprimir(tablero) # funcion del juego
        #f.imprimido(tablero) # función para ver la matriz
        #f.imprimicion(tablero) # funcion para ver los W, P y G
        movimiento = str(input("Ingrese movimiento: ")).upper()
        if str(movimiento).upper() == "H":
            dic_partidas[partida] = [tablero, y, x, jugadas, breik, orito, n, flecha]
            print("PARTIDA GUARDADA EXITOSAMENTE".center(75))
            break
        x, y, jugadas, flecha, tablero, breik = f.moverse(movimiento, x, y, jugadas, tablero, n, flecha, breik)
        breik, orito = f.verificarposiciones(breik, orito, tablero, x, y)
        if breik == True:
            f.imprimir(tablero)
            print(f"Jugadas totales: {jugadas}.".center(75))
            dic_partidas[partida] = ""
            break

with open("data.json", "r") as archivo:
    dic_partidas = json.load(archivo)

while True: # MENÚ DE CARGA
    print('\n' + "\033[38;2;74;241;28m" + ' MENÚ '.center(75, '-') + '\033[0m')
    print('1: Nueva Partida'.center(75))
    print('2: Cargar Partida'.center(75))
    print('3: Guía de juego'.center(75))
    print('4: Reiniciar'.center(75))
    print('5: Salir'.center(75))
    print("\033[38;2;74;241;28m" + ''.center(75, '-') + '\033[0m')

    opcion = input('Elija una opción: ') # ELEGIR OPCIÓN
    while opcion not in ["1", "2", "3", "4", "5"]:
        opcion = input('\033[38;2;255;0;0m' + 'Opción inválida. ' + "\033[0m" + 'Elija una opción: ')

    if opcion == "1":
        print('\n' + 'Crear una Nueva Partida'.center(75) + '\n')
        print('1: Partida 1'.center(75))
        print('2: Partida 2'.center(75))
        print('3: Partida 3'.center(75))
        print('4: Partida 4'.center(75))
        print('5: Partida 5'.center(75))
        print('H: Menú'.center(75))
        print()

        while True:
            partida = input("Elegir Partida: ")
            if partida in ["1", "2", "3", "4", "5"]:
                if dic_partidas[partida] == "":

                    tablero, y, x, jugadas, breik, orito, n, flecha = f.crear_datos() # CREAR DATOS
                    juego(tablero, y, x, jugadas, breik, orito, n, flecha) # JUEGO
                    break # TÉRMINO DE LA PARTIDA

                else:
                    print("Partida existente, ¿desea sobreescribir la partida?".center(75))
                    decision = input("SÍ / NO : ")
                    if str(decision).upper() in ["SI", "SÍ"]:

                        tablero, y, x, jugadas, breik, orito, n, flecha = f.crear_datos() # CREAR DATOS
                        juego(tablero, y, x, jugadas, breik, orito, n, flecha) # JUEGO
                        break # TÉRMINO DE LA PARTIDA

                    else:
                        print("La partida no se sobreescribió.".center(75))
                        continue
            elif str(partida).upper() == "H":
                break
            else:
                print('\033[38;2;255;0;0m' + "Partida inválida." + "\033[0m", end=" ")
                continue

    elif opcion == "2":
        print('\n' + 'Elija una partida'.center(75) + '\n')
        print('1: Partida 1'.center(75))
        print('2: Partida 2'.center(75))
        print('3: Partida 3'.center(75))
        print('4: Partida 4'.center(75))
        print('5: Partida 5'.center(75))
        print('H: Menú'.center(75))
        print()

        while True:
            partida = input("Elegir Partida: ")
            if partida in ["1", "2", "3", "4", "5"]:
                if dic_partidas[partida] == "":
                    print("La partida elegida no contiene datos, elija una partida válida".center(75))
                    continue
                else:
                    # RECIBIR DATOS ALMACENADOS
                    tablero = dic_partidas[partida][0]
                    y = dic_partidas[partida][1]
                    x = dic_partidas[partida][2]
                    jugadas = dic_partidas[partida][3]
                    breik = dic_partidas[partida][4]
                    orito = dic_partidas[partida][5]
                    n = dic_partidas[partida][6]
                    flecha = dic_partidas[partida][7]

                    breik, orito = f.verificarposiciones(breik, orito, tablero, x, y)
                    juego(tablero, y, x, jugadas, breik, orito, n, flecha) # JUEGO
                    break # TÉRMINO DE LA PARTIDA

            elif str(partida).upper() == "H":
                break
            else:
                print('\033[38;2;255;0;0m' + "Partida inválida." + "\033[0m", end=" ")
                continue

    elif opcion == "3":
        f.guia()

    elif opcion == "4":
        print("¿Estás seguro que deseas borrar todos los datos de las partidas existentes?".center(75))
        decision = input("SÍ / NO : ")
        if str(decision).upper() in ["SI", "SÍ"]:
            dic_partidas["1"] = ""
            dic_partidas["2"] = ""
            dic_partidas["3"] = ""
            dic_partidas["4"] = ""
            dic_partidas["5"] = ""
            print("LOS DATOS DE LAS PARTIDAS FUERON BORRADOS.".center(75))
        else:
            print("Los datos de las partidas no se borraron.".center(75))

    elif opcion == "5": #CREDITOS
        print('\n' + "".center(75, '-'))
        print('\n' + "¡Gracias por jugar WUMPUS! Esperamos que te haya gustado.".center(75) + '\n')
        print('\033[1m' + "CRÉDITOS".center(75))
        print('\033[94m' + "Samanta Chang".center(75))
        print("Fiorella Falcón".center(75))
        print("Delia Juy".center(75) +'\n')
        print("\033[38;2;246;240;37m" +             '|\/\/|'.center(75))
        print(                                      '~~~~~~'.center(75))
        print("\033[38;2;221;67;23m" +                '__'.center(75))
        print(                                     '__|  |__'.center(75))
        print(                                   '_|        |_'.center(75))
        print("\033[38;2;246;131;32m" +         '|   _    _   |'.center(75))
        print(                            ' _    |  |_|  |_|  |     _'.center(75))
        print("\033[38;2;246;240;37m" +  ' |_|_ _| /// ww /// | _ _|_|'.center(75))
        print(                           ' |_|_|_|            ||_|_|_|'.center(75))
        print("\033[38;2;74;241;28m" +          '|    ____    |'.center(75))
        print(                                  '|_|_|    |_|_|'.center(75))
        print("\033[38;2;28;161;240m" +         '|_|_|    |_|_|'.center(75))
        print(                                  '|_|_|    |_|_|'.center(75))
        print("\033[38;2;133;96;217m" +        '_|_|_|    |_|_|_'.center(75))
        print(                                '|_|_|_|    |_|_|_|'.center(75) + "\033[0m")

        print('\n' + '\033[0m' + ' FIN DEL JUEGO '.center(75, '-'))
        break

with open("data.json", "w") as archivo:
    json.dump(dic_partidas, archivo)
