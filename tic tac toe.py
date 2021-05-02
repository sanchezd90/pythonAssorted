'#Variables declaradas e inicializadas'
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
currentToken = "X"
winningToken = ""
slotsFilled = 0

'#Avisos e instrucciones'
print("Tic-Tac-Toe")
print("No hace falta explicar el juego")
print("Comienza el jugador 1 con la X, luego el jugador 2 con el O")

'#Loop principal'
while winningToken == "" and slotsFilled < 9:
    print("\n")
    print("%s|%s|%s" % (board[0], board[1], board[2]))
    print("-+-+-")
    print("%s|%s|%s" % (board[3], board[4], board[5]))
    print("-+-+-")
    print("%s|%s|%s" % (board[6], board[7], board[8]))
    pos = -1
    '#Loop para pedir posición y validarla'
    while (pos == -1):
        pos = int(input("\nEs el turno de %s. Elija una posición: " % currentToken))
        if pos < 1 or pos > 9:
            pos = -1
            print("Posición no válida! Debe elegir un número entre 1y 9.")
        pos = pos - 1
        if board[pos] == "X" or board[pos] == "O":
            pos = -1
            print("Ese lugar ya fue ocupado por ∞s! Intente nuevamente" % board[pos])
    '#Cambio del board por la jugada'
    board[pos] = currentToken
    slotsFiller = slotsFilled + 1
    '#Estado de las filas'
    row1 = board[0] == currentToken and board[1] == currentToken and board[2] == currentToken
    row2 = board[3] == currentToken and board[4] == currentToken and board[5] == currentToken
    row3 = board[6] == currentToken and board[7] == currentToken and board[8] == currentToken
    '#Estado de las columnas'
    col1 = board[0] == currentToken and board[1] == currentToken and board[2] == currentToken
    col2 = board[3] ==currentToken and board[4] == currentToken and board[5] == currentToken
    col3 = board[6] ==currentToken and board[7] == currentToken and board[8] == currentToken
    '#Estado de las diagonales'
    diag1 = board[0] == currentToken and board[4] == currentToken and board[8] == currentToken
    diag2 = board[2] == currentToken and board[4] == currentToken and board[6] == currentToken
    '#Revision del board'
    row = row1 or row2 or row3
    col = col1 or col2 or col3
    diag = diag1 or diag2
    if (row or col or diag):
        print("\n")
        print("%s|%s|%s" % (board[0], board[1], board[2]))
        print("-+-+-")
        print("%s|%s|%s" % (board[3], board[4], board[5]))
        print("-+-+-")
        print("%s|%s|%s" % (board[6], board[7], board[8]))
        print("Felicitaciones %s! Has ganado!" % currentToken)
        winningToken = currentToken
    if currentToken == "X":
        currentToken = "O"
    else:
        currentToken = "X"
    if slotsFilled == 9 and winningToken == "":
        print("Nadie ganó. Suerte en la próxima ronda!")
