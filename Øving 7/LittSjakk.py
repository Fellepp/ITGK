def make_board(board_string):
    board = [[None for i in range(5)] for i in range(5)]
    boardList = list(board_string)
    for i in range(5):
        for j in range(5):
            if boardList[j + 5*i] == ".":
                continue
            board[i][j] = boardList[j + 5*i]
    return board

def printChessBoard(lst, n):
    for i in range(n):
        print(lst[i])

#b)
def get_piece(board, y, x):
    xPos = 6-x
    yPos = y
    print(xPos-1, yPos-1)
    brikke = board[xPos-1][yPos-1]
    return brikke

def get_legal_moves(board, x, y):
    if x > 5 or y > 5 or x < 1 or y < 1:
        return "Error"

    print("\n Leggo \n") #Går ut ifra svart brikke
    moves = []
    isWhite = False
    startPos = 4
    retning = -1
    brikke = get_piece(board, x, y)
    langtForan = 0
    foran = 0
    skrå1 = 0
    skrå2 = 0
    print(brikke)

    if brikke is None: #Sjekker om det er en brikke på plassen, hvis ikke, return tom liste
        return moves

    if 65 <= ord(brikke) <= 90: #Sjekker om stor bokstav, hvis ja, brikke er hvit
        isWhite = True
        startPos = 2

    if isWhite: #Hvis hvit, går oppover, hvis svart, går nedover
        retning = 1
    print(retning)

    if (isWhite and y == 2) or (not isWhite and y == 4):
        if (y < 4 or not isWhite) and (y > 2 or isWhite):
            langtForan = get_piece(board, x, y + 2*retning)
            if langtForan is None:
                tall1 = x
                tall2 = y + 2*retning
                moves.append((tall1, tall2))

    if (y < 5 or not isWhite) and (y>1 or isWhite): #Hvis raden er mindre enn 5 eller brikken er svart - Den kan gå framover
        foran = get_piece(board, x, y+retning)
        if foran is None:
            tall1 = x
            tall2 = y+retning
            moves.append((tall1, tall2))
        if x+1 <= 5: #Den kan gå til høyre
            skrå1 = get_piece(board, x+1, y+retning)
            if skrå1 is not None: #Det er en brikke der
                if (ord(skrå1) > 90 and isWhite) or (ord(skrå1) <= 90 and not isWhite): #Hvis fiende
                    tall1 = x+1
                    tall2 = y+retning
                    moves.append((tall1, tall2))
        if x-1 >= 1: #Den kan gå til venstre
            skrå2 = get_piece(board, x-1, y+retning)
            if skrå2 is not None: #Det er en brikke der
                if (ord(skrå2) > 90 and isWhite) or (ord(skrå2) <= 90 and not isWhite): #Hvis fiende
                    tall1 = x-1
                    tall2 = y+retning
                    moves.append((tall1, tall2))


    return moves, brikke, langtForan, foran, skrå1, skrå2



board = make_board("rkn.r.p.....P..PP.PPB.K..")
printChessBoard(board, 5)
print(get_piece(board, 2, 1))
##print(get_piece(board, 5, 5))

print(get_legal_moves(board, 2, 4))