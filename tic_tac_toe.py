board = [[" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]]

def displayboard():
    for space in range(3):
        print(" ", board[space][space], "│", board[space][space], "│", board[space][space])
        if space < 2:
            print(" ───┼───┼─── ")

def tictactoe():
    
    end = False

    displayboard()

    while end == False:
        P1play = input("Player 1 moves, input x and y: ")
        P1play = P1play.split()
        board[P1play[0], P1play[1]] = "X"
        displayboard()



tictactoe()