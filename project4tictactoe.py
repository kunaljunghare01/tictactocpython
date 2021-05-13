#Tic tac toe game
#input for loop for asking to play game
#input for 9  values
#user move
#computer move
#any free space
#winner
#post work afer win winner

#algorithm
#1)input
#2)design the board
#3)is there a free space
#4)is winner
#5)player move
#6)computer move
#7)main logic
#8)interface


#board which should contain 9 space 
board = [' ' for x in range(10)]
#input we are taking from user
def insertletter(letter,pos):
    #it will fill the position with that letter "x or o"
    board[pos] = letter 

def spaceisFree(pos):
    return board[pos] == ' '

def printBoard(board):
    print('   |    |   ')
    print(' '+ board[1]  +' | '+ board[2] +'  |  ' + board[3])
    print('   |    |   ')
    print('------------')
    print('   |    |   ')
    print(' '+ board[4] + ' | ' + board[5] + '  |  ' + board[6])
    print('   |    |   ')
    print('------------')
    print('   |    |   ')
    print(' '+ board[7] + ' | ' + board[8] + '  |  ' + board[9])
    print('   |    |   ')


def isBoardFull(board):
    if board.count(' ')>1:
        return False
    else:
        return True

def isWinner(b,l):
    return ((b[1]==l and b[2]==l and b[3]==l) or (b[4]==l and b[5]==l and b[6]==l)  or (b[7]==l and b[8]==l and b[9]==l)  or (b[1]==l and b[4]==l and b[7]==l)  or (b[2]==l and b[5]==l and b[8]==l)  or (b[3]==l and b[6]==l and b[9]==l)  or (b[1]==l and b[5]==l and b[9]==l)  or (b[7]==l and b[5]==l and b[3]==l))  


def playerMove():
    run = True
    while run:
        move = input("please select a position to enter the x between 1 to 9")
        try:
            move = int(move)
            if move>0 and move<10:
                if spaceisFree(move):
                    run = False
                    insertletter('X', move)

                else:
                    print("Sorry ,this space is occupied")

            else:
                print("Wrong input")

        except:
            print("Please type a number")


def computerMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x is not 0]
    move = 0

    for let in ['0','X']:
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if isWinner(boardcopy, let):
                move = i
                return move


    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move


def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def main():
    print("Welcome to the Game")
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, '0')):
            playerMove()
            printBoard(board)

        else:
            print("Sorry u lose")
            break


        if not(isWinner(board, 'X')):
            move = computerMove()
            if move == 0:
                print(" ")

            else:
                insertletter('0', move)
                print('Computer placed 0 an a position',move,":")
                printBoard(board)

        else:
            print("u win")
            break



    if isBoardFull(board):
        print("Tie Game")
    
while True:
    x = input("Do u want to play again? (y/n)")
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print('--------------------------')
        main()

    else:
        break



