import random

bombProbability = 7   # 0-100%
boardLength = 25
boardHeight = 25

def printBoard(board):
    for row in board:
        aux = []
        for elem in row:
            if elem != "*":
                if elem == 0:
                    aux.append(" ")
                else:
                    aux.append(elem)
            else:
                aux.append(elem)
        print(' '.join(map(str, aux)))
    print()

def generateBombs(boardLength, boardHeight, bombProb):
    board = []

    for row in range(0, boardHeight):
        board.append([])
        for col in range(0, boardLength):
            rand = random.randint(1,100)

            if rand < bombProb:
                board[row].append("*")
            else:
                board[row].append(0)

    return board

def generateNumbers(board):
    for i, row in enumerate(board):
        for j, elem in enumerate(row):
            count = 0
            if elem != "*":
                if i - 1 >= 0:
                    if board[i-1][j] == "*":                # i - 1, j
                        count += 1
                    if j - 1 >= 0:
                        if board[i - 1][j - 1] == "*":      # i - 1, j - 1
                            count += 1
                    if j + 1 < boardLength:
                        if board[i - 1][j + 1] == "*":      # i - 1, j + 1
                            count += 1

                if i + 1 < boardHeight:
                    if board[i+1][j] == "*":                # i + 1, j
                        count += 1
                    if j - 1 >= 0:
                        if board[i + 1][j - 1] == "*":      # i + 1, j - 1
                            count += 1
                    if j + 1 < boardLength:
                        if board[i + 1][j + 1] == "*":      # i + 1, j + 1
                            count += 1

                if j - 1 >= 0:
                    if board[i][j-1] == "*":                # i, j - 1
                        count += 1

                if j + 1 < boardLength:
                    if board[i][j+1] == "*":                # i, j + 1
                        count += 1
                board[i][j] = count

    return board

# ----------- MAIN -----------

board = generateBombs(boardLength, boardHeight, bombProbability)
board = generateNumbers(board)

printBoard(board)