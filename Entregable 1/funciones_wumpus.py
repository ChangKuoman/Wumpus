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

dibujo_wumpus = ['__',
               '_|  |_',
             '_|      |_',
            '|  _    _  |',
            '| |_|  |_| |',
         '_ _|  _ WW _  |_ _',
        '|_|_|_| |__| |_|_|_|',
          '|_|_|      |_|_|',
            '|_|      |_|']

texto_movimiento = ["Para Moverte usa las teclas WASD",
                    "Usa W para moverte hacia arriba",
                    "Usa A para moverte hacia la izquierda",
                    "Usa S para moverte hacia abajo",
                    "Usa D para moverte hacia la derecha"]
dimesiones_texto = ["Dimensión de tablero mínimo: 4",
                    "Mínimo de pits: 1",
                    "Máximo de pits: dimensión del tablero - 1",
                    "Mínimo de wumpus: 1",
                    "Máximo de wumpus: dimensión del tablero - 1"]

for i in texto_bienvenida:
    print('\033[94m' + i.center(75) + '\033[0m')
print()
for i in dibujo_wumpus:
    print('\033[94m' + i.center(75) + '\033[0m')
print()
print('\033[93m' + ' Guía de movimiento '.center(75, '-') + '\033[0m')
for i in texto_movimiento:
    print(i.center(75))
print()
print('\033[93m' + ' Guía de dimensiones '.center(75, '-') + '\033[0m')
for i in dimesiones_texto:
    print(i.center(75))
print()

"""
· --> blanc (con fill)
O --> personaje (posición inicial : siempre en (-1, 0)
W --> wumpus (aleatorio)
G --> gold (aleatorio)
S --> stench (lado al wumpus)
P --> pit (aleatorio)
B --> breeze (lado del pit)
"""

#funciones impresión:
def imprimir(matriz): #juego
    print()
    for i in matriz:
        x = ''
        for j in i:
            #print(j[0], end=" ")
            x += j[0] + ' '
        #print()
        print(x.center(75))
    print()

def imprimido(matriz): #verificar matriz
    for i in matriz:
        for j in i:
            print(f'{j} \t', end="")
        print()

#funciones de creación de tablero:
def crearTablero(n): #crear tablero de n
    tablero = [[["·"] for i in range(n)] for j in range(n)]
    tablero[-1][0][0] = "O"
    return tablero

def crearWumpus(tablero, n, wumpus): #crear wumpus
    for i in range(wumpus):

        tablero[rd(0, n-1)][rd(0, n-1)].append('W')
        while "W" in tablero[-1][0] or "W" in tablero[-2][0] or 'W' in tablero[-1][1]:
            tablero[-1][0] = ["O"]
            tablero[-2][0] = ['·']
            tablero[-1][1] = ['·']
            tablero[rd(0, n-1)][rd(0, n-1)].append('W')

    return tablero

def positionStench(tablero, n): #crear estench y oro
    for i in range(n):
        for j in range(n):

            if 'W' in tablero[(i+1)%n][j] and i != n-1:
                tablero[i][j].append('S')

            if 'W' in tablero[(i-1)%n][j] and i != 0:
                tablero[i][j].append('S')

            if 'W' in tablero[i][(j+1)%n] and j != n-1:
                tablero[i][j].append('S')

            if 'W' in tablero[i][(j-1)%n] and j != 0:
                tablero[i][j].append('S')

    return tablero

def crearPits(tablero, n, pits): #crear pits
    for i in range(pits):

        tablero[rd(0, n-1)][rd(0, n-1)].append('P')

        while "P" in tablero[-1][0] or "P" in tablero[-2][0] or 'P' in tablero[-1][1]:
            tablero[-1][0] = ["O"]
            tablero[-2][0] = ['·']
            tablero[-1][1] = ['·']
            tablero[rd(0, n-1)][rd(0, n-1)].append('P')

    return tablero

def positionBreeze(tablero, n): #crear breeze

    for i in range(n):
        for j in range(n):

            if 'P' in tablero[(i+1)%n][j] and i != n-1:
                tablero[i][j].append('B')

            if 'P' in tablero[(i-1)%n][j] and i != 0:
                tablero[i][j].append('B')

            if 'P' in tablero[i][(j+1)%n] and j != n-1:
                tablero[i][j].append('B')

            if 'P' in tablero[i][(j-1)%n] and j != 0:
                tablero[i][j].append('B')
    return tablero

def crearGold(tablero, n): #crear gold
    a, b = rd(0, n-1), rd(0, n-1)
    tablero[a][b].append('G')
    while 'P' in tablero[a][b] or 'W' in tablero[a][b] or "G" in tablero[-1][0] or "G" in tablero[-2][0] or 'G' in tablero[-1][1]:
        while "G" in tablero[-1][0] or "G" in tablero[-2][0] or 'G' in tablero[-1][1]:
            tablero[-1][0] = ["O"]
            tablero[-2][0] = ['·']
            tablero[-1][1] = ['·']
            a, b = rd(0, n-1), rd(0, n-1)
            tablero[a][b].append('G')

        while 'P' in tablero[a][b] or 'W' in tablero[a][b]:
            tablero[a][b].remove("G")
            a, b = rd(0, n-1), rd(0, n-1)
            tablero[a][b].append('G')
    return tablero

#funciones del juego en sí:
def moverse(mov, x, y, jugadas, tablero, n): #función moverse

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

    elif mov == "PYTHON":
        print('\033[1m' + "EASTER EGG: print('Hello World!')".center(75) + '\033[0m')

    elif mov == "UTEC":
        print( '\033[1m' + "EASTER EGG: UTEC. CARRERAS QUE MUEVEN EL MUNDO".center(75) + '\033[0m')

    else: print("Recuerda que el movimiento es con WASD.".center(75))
    return x, y, jugadas

def verificarposiciones(breik, orito, tablero, x, y): #verificar posiciones

    if "W" in tablero[y][x]:
        print('\033[91m' + "GAME OVER. Te comió el wumpus.".center(75) + '\033[0m')
        breik = True
    elif "P" in tablero[y][x]:
        print('\033[91m' + "GAME OVER. ¡Te caiste por un hoyo! ".center(75) + '\033[0m')
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
            print('\033[92m' + "¡Ganaste el juego!".center(75) + '\033[0m')
            breik = True
    return breik, orito