```py
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']
currentPlayer = "X"
winner = None
gameRunning = True


# printing the board

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("-" * 10)
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("-" * 10)
    print(board[6] + " | " + board[7] + " | " + board[8])


# take player input
"""
1  |  2  |  3
4  |  5  |  6
7  |  8   | 9
"""


def playerInput(board):
    while True:
        if currentPlayer == "X":
            inp = int(input("player(1)  Enter a number from 1-9 :"))
        else:
            inp = int(input("Player(2) Enter a number from 1-9 :"))
        if inp >= 1 and inp <= 9 and board[inp - 1] == "-":
            board[inp - 1] = currentPlayer
            break
        else:
            if currentPlayer == "X":
                print("Try again Player (1) !  player (2) in that spot")
            else:
                print("Try again Player(2) !   Player (1)  in that spot ")
            printBoard(board)


# check for win or tie
def checkHorizontal(board):
    global winner
    if (board[0] == board[1] == board[2] and board[0] != "-") or (
            board[3] == board[4] == board[5] and board[3] != "-") or (
            board[6] == board[7] == board[8] and board[6] != "-"):
        winner = currentPlayer
        return True


def checkRow(board):
    global winner
    if (board[0] == board[3] == board[6] and board[0] != "-") or (
            board[1] == board[4] == board[7] and board[1] != "-") or (
            board[2] == board[5] == board[8] and board[2] != "-"):
        winner = currentPlayer
        return True


def checkDiagonal(board):
    global winner
    if (board[0] == board[4] == board[5] and board[0] != "-") or (board[2] == board[4] == board[6] and board[2] != "-"):
        winner = currentPlayer
        return True


def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("Its a tie")
        gameRunning = False


def checkWin():
    if checkDiagonal(board) or checkHorizontal(board) or checkRow(board):
        print(f"The winner is {winner} ")


# switch the player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


# check for win or tie again

while gameRunning:
    printBoard(board)
    if winner != None:
        break
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
  ```
