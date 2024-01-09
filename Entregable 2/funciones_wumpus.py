from random import randint as rd

#Interfaz de usuario ----------------------------------------------

texto_bienvenida = [" ____  ____  ____  _  _  _  _  ____  _  _  ____  ____   ____  ___ ",
                    "(  - \(_  _)( ___)( \( )( \/ )( ___)( \( )(_  _)(  _ \ ( ___)/ __)",
                    " ) _ < _)(_  )__)  )  (  \  /  )__)  )  (  _)(_  )(_) ) )__) \__ |",
                    "(____/(____)(____)(_)\_)  \/  (____)(_)\_)(____)(____/ (____)(___/",
                    "   "  ,
                    "   __        _    _  __  __  __  __  ____  __  __  ___ ",
                    "  /__\      ( \/\/ )(  )(  )(  \/  )(  _ \(  )(  )/ __)",
                    " /(  )\      )    (  )(__)(  )    (  )___/ )(__)( \__ |",
                    "(__)(__)    (__/\__)(______)(_/\/\_)(__)  (______)(___/"]

texto_juego = ["Te encuentras en una cueva oscura y misteriosa,",
               "tu misión es encontrar el oro y salir a salvo de la cueva.",
               "Ten cuidado con los wumpus, monstruos misteriosos",
               "que te atrapan haciendote perder. También ten cuidado",
               "con los hoyos porque te puedes caer.",
               "¡Buena suerte en tu aventura!"]
texto_movimiento = ["Para Moverte usa las teclas WASD",
                    "Usa W para moverte hacia arriba",
                    "Usa A para moverte hacia la izquierda",
                    "Usa S para moverte hacia abajo",
                    "Usa D para moverte hacia la derecha",
                    "Usa F para lanzar una única flecha y matar al Wumpus",
                    "Usa H para regresar al menú principal"]
dimesiones_texto = ["Dimensión de tablero mínimo: 4",
                    "Mínimo de hoyos: 1",
                    "Máximo de hoyos: dimensión del tablero - 1",
                    "Mínimo de wumpus: 1",
                    "Máximo de wumpus: dimensión del tablero - 1"]

for i in texto_bienvenida:
    print('\033[94m' + i.center(75) + '\033[0m')
print()

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

def guia():
    print()
    print("\033[38;2;246;240;37m" + ' Guía de juego '.center(75, '-') + '\033[0m')
    for i in texto_juego:
        print(i.center(75))
    print()
    print("\033[38;2;246;240;37m" + ' Guía de movimiento '.center(75, '-') + '\033[0m')
    for i in texto_movimiento:
        print(i.center(75))
    print()
    print("\033[38;2;246;240;37m" + ' Guía de dimensiones '.center(75, '-') + '\033[0m')
    for i in dimesiones_texto:
        print(i.center(75))

guia()

# · --> blanc (con fill)
# O --> personaje (posición inicial : siempre en (-1, 0)
# W --> wumpus (aleatorio)
# G --> gold (aleatorio)
# S --> stench (al lado de wumpus)
# P --> pit (aleatorio)
# B --> breeze (al lado de pit)

# FUNCIONES DE IMPRESIÓN
def imprimir(matriz): # JUEGO
    print()
    for i in matriz:
        x = ''
        for j in i:
            x += j[0] + ' '
        print(x.center(75))
    print()

def imprimido(matriz): # VERIFICACIÓN DE MATRIZ
    for i in matriz:
        for j in i:
            print(f'{j} \t', end="")
        print()

def imprimicion(matriz): # Muestra las cosas segun
    for i in matriz:
        for j in i:
            if "W" in j:
                print("W", end=" ")
            elif "P" in j:
                print("P", end=" ")
            elif "O" in j:
                print("O", end=" ")
            elif "G" in j:
                print("G", end=" ")
            else:
                print("·", end=" ")
        print()

# FUNCION CREACIÓN DE DATOS
def crear_datos():
    n = input('\n' + 'Ingrese dimensión del tablero: ')
    while True:
        if n.isdigit():
            n = int(n)
            if n >= 4:
                break
        n = input('\n' + '\033[38;2;255;0;0m' + 'Valor inválido. ' + '\033[0m' + 'Ingrese un' + '\033[38;2;255;0;0m' + ' NÚMERO ' + '\033[0m' + 'mayor o igual a 4: ')

    pits = input('\n' + 'Ingrese número de hoyos: ')
    while True:
        if pits.isdigit():
            pits = int(pits)
            if pits >= 1 and pits <= n - 1:
                break
        pits = input('\n' + '\033[38;2;255;0;0m' + 'Valor inválido. ' + '\033[0m' + 'Ingrese número VÁLIDO de hoyos: ')

    wumpus = input('\n' + 'Ingrese número de wumpus: ')
    while True:
        if wumpus.isdigit():
            wumpus = int(wumpus)
            if wumpus >= 1 and wumpus <= n - 1:
                break
        wumpus = input('\n' + '\033[38;2;255;0;0m' + 'Valor inválido. '+ '\033[0m' + 'Ingrese número VÁLIDO de wumpus: ')

    # CREAR TABLERO
    tablero = crearTablero(n)
    crearWumpus(tablero, n, wumpus)
    crearPits(tablero, n, pits)
    crearGold(tablero, n)

    # VARIABLES
    y = n - 1
    x = 0
    jugadas = 0
    breik = False
    orito = False
    flecha = True
    return tablero, y, x, jugadas, breik, orito, n, flecha

# FUNCIONES PARA LA CREACIÓN DEL TABLERO
def crearTablero(n): # CREAR TABLERO DE N
    tablero = [[["·"] for i in range(n)] for j in range(n)]
    tablero[-1][0][0] = "O"
    return tablero

def crearWumpus(tablero, n, wumpus): # CREAR WUMPUS Y STENCH
    for i in range(wumpus):
        a, b = rd(0, n-1), rd(0, n-1)
        tablero[a][b].append('W')
        while "W" in tablero[-1][0] or "W" in tablero[-2][0] or 'W' in tablero[-1][1]:
            if "W" in tablero[-1][0]: tablero[-1][0].remove("W")
            if "W" in tablero[-2][0]: tablero[-2][0].remove("W")
            if "W" in tablero[-1][1]: tablero[-1][1].remove("W")
            a, b = rd(0, n-1), rd(0, n-1)
            tablero[a][b].append('W')

        if a + 1 != n:
            tablero[a+1][b].append("S")
        if b + 1 != n:
            tablero[a][b+1].append("S")
        if a - 1 != -1:
            tablero[a-1][b].append("S")
        if b - 1 != -1:
            tablero[a][b-1].append("S")
    return tablero

def crearPits(tablero, n, pits): # CREAR PITS Y BREEZE
    for i in range(pits):
        a, b = rd(0, n-1), rd(0, n-1)
        tablero[a][b].append('P')
        while "P" in tablero[-1][0] or "P" in tablero[-2][0] or 'P' in tablero[-1][1]:
            if "P" in tablero[-1][0]: tablero[-1][0].remove("P")
            if "P" in tablero[-2][0]: tablero[-2][0].remove("P")
            if "P" in tablero[-1][1]: tablero[-1][1].remove("P")
            a, b = rd(0, n-1), rd(0, n-1)
            tablero[a][b].append('P')

        if a + 1 != n:
            tablero[a+1][b].append("B")
        if b + 1 != n:
            tablero[a][b+1].append("B")
        if a - 1 != -1:
            tablero[a-1][b].append("B")
        if b - 1 != -1:
            tablero[a][b-1].append("B")
    return tablero

def crearGold(tablero, n): # CREAR GOLD
    a, b = rd(0, n-1), rd(0, n-1)
    tablero[a][b].append('G')
    while 'P' in tablero[a][b] or 'W' in tablero[a][b] or "G" in tablero[-1][0] or "G" in tablero[-2][0] or 'G' in tablero[-1][1]:
        while "G" in tablero[-1][0] or "G" in tablero[-2][0] or 'G' in tablero[-1][1]:
            if "G" in tablero[-1][0]: tablero[-1][0].remove("G")
            if "G" in tablero[-2][0]: tablero[-2][0].remove("G")
            if "G" in tablero[-1][1]: tablero[-1][1].remove("G")
            a, b = rd(0, n-1), rd(0, n-1)
            tablero[a][b].append('G')

        while 'P' in tablero[a][b] or 'W' in tablero[a][b]:
            tablero[a][b].remove("G")
            a, b = rd(0, n-1), rd(0, n-1)
            tablero[a][b].append('G')
    return tablero

# FUNCIONES DEL JUEGO
def moverse(mov, x, y, jugadas, tablero, n, flecha, breik): #FUNCIÓN DEL MOVIMIENTO

    if mov == "W":
        if y - 1 == -1: print("Te chocaste contra la pared. ¡No puedes ir por ahí!".center(75))
        else:
            tablero[y][x][0] = "·"
            y -= 1
            tablero[y][x][0] = "O"
            jugadas += 1

    elif mov == "S":
        if y + 1 == n: print("Te chocaste contra la pared. ¡No puedes ir por ahí!".center(75))
        else:
            tablero[y][x][0] = "·"
            y += 1
            tablero[y][x][0] = "O"
            jugadas += 1

    elif mov == "D":
        if x + 1 == n: print("Te chocaste contra la pared. ¡No puedes ir por ahí!".center(75))
        else:
            tablero[y][x][0] = "·"
            x += 1
            tablero[y][x][0] = "O"
            jugadas += 1

    elif mov == "A":
        if x - 1 == -1: print("Te chocaste contra la pared. ¡No puedes ir por ahí!".center(75))
        else:
            tablero[y][x][0] = "·"
            x -= 1
            tablero[y][x][0] = "O"
            jugadas += 1

    elif mov == "F" and flecha == False:
        print("No tienes flecha para tirar!".center(75))

    elif mov == "F" and flecha == True:
        flecha = False
        a, b = rd(0, n-1), rd(0, n-1)
        if 'W' in tablero[a][b]:
            tablero[a][b].remove("W")
            if a + 1 != n:
                tablero[a+1][b].remove("S")
            if b + 1 != n:
                tablero[a][b+1].remove("S")
            if a - 1 != -1:
                tablero[a-1][b].remove("S")
            if b - 1 != -1:
                tablero[a][b-1].remove("S")
            print("¡Mataste a un Wumpus!".center(75))
        elif "O" in tablero[a][b]:
            print('\033[38;2;255;0;0m' + "GAME OVER. La flecha cayó sobre tí.".center(75) + '\033[0m')
            breik = True
        else: print("No mataste ningún Wumpus".center(75))

    elif mov == "PYTHON":
        print('\033[1m' + "EASTER EGG: print('Hello World!')".center(75) + '\033[0m')

    elif mov == "UTEC":
        print( '\033[1m' + "EASTER EGG: UTEC. CARRERAS QUE MUEVEN EL MUNDO".center(75) + '\033[0m')

    else: print("Recuerda que el movimiento es con WASD.".center(75))
    return x, y, jugadas, flecha, tablero, breik

def verificarposiciones(breik, orito, tablero, x, y): # VERIFICAR POSICIONES

    if "W" in tablero[y][x]:
        print('\033[38;2;255;0;0m' + "GAME OVER. Te comió el wumpus.".center(75) + '\033[0m')
        breik = True
    elif "P" in tablero[y][x]:
        print('\033[38;2;255;0;0m' + "GAME OVER. ¡Te caiste por un hoyo! ".center(75) + '\033[0m')
        breik = True
    else:
        if "S" in tablero[y][x]:
            print("¡Wumpus cerca!".center(75))
        if "B" in tablero[y][x]:
            print("Hay un hueco cerca. ¡Ten cuidado!".center(75))
        if "G" in tablero[y][x]:
            print("¡Agarraste el oro! Ahora vuelve al inicio para ganar.".center(75))
            orito = True
            tablero[y][x].remove("G")
        if "O" in tablero[-1][0] and orito == True:
            print("\033[38;2;74;241;28m" + "¡Ganaste el juego!".center(75) + '\033[0m')
            breik = True
    return breik, orito
