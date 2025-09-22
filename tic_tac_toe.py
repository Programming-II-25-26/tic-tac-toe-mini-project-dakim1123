board = [[" ", " ", " "],
       [" ", " ", " "],
       [" ", " ", " "]]


def intro():
   print("Welcome to Tic-Tac-Toe!")
   print("------------------------")
   print("Rules:")
   print("1. Player 1 is X, Player 2 is O.")
   print("2. Players take turns placing their marks on the 3x3 grid.")
   print("3. Enter a number from 1 to 9 to place your mark, as shown below:")
   print(" 1 │ 2 │ 3 ")
   print("───┼───┼───")
   print(" 4 │ 5 │ 6 ")
   print("───┼───┼───")
   print(" 7 │ 8 │ 9 ")
   print("Get three in a row (horizontally, vertically, or diagonally) to win.")
   print("Good luck!")


def displayboard():
   for space in range(3):
       print(" ", board[space][0], "│", board[space][1], "│", board[space][2])
       if space < 2:
           print(" ───┼───┼─── ")


def getpo(play):
   if 1 <= play <= 9:
       row = (play - 1) % 3
       if play <= 3:
           col = 0
       elif play <= 6:
           col = 1
       else:
           col = 2
          
       return row, col
   else:
       return None
  
def check_win(board, symbol):
   win = False
   if board[0][0] == symbol and board[0][1] == symbol and board[0][2] == symbol:
       win = True
       return True
   elif board[1][0] == symbol and board[1][1] == symbol and board[1][2] == symbol:
       win = True
       return True
   elif board[2][0] == symbol and board[2][1] == symbol and board[2][2] == symbol:
       win = True
       return True
   elif board[0][0] == symbol and board[1][0] == symbol and board[2][0] == symbol:
       win = True
       return True
   elif board[0][1] == symbol and board[1][1] == symbol and board[2][1] == symbol:
       win = True
       return True
   elif board[0][2] == symbol and board[1][2] == symbol and board[2][2] == symbol:
       win = True
       return True
   elif board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
       win = True
       return True
   elif board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol:
       win = True
       return True
   return False




def tictactoe():
  
   intro()


   win = False


   displayboard()


   playernum = 0


   while not win:
       if playernum % 2 == 0:
           symbol = "X"
           oppsymbol = "O"
       else:
           symbol = "O"
           oppsymbol = "X"


       ask = input(f'Player {playernum % 2 + 1} plays, input position from 1 - 9: ')


       try:
           play = int(ask)
       except ValueError:
           print("Please enter a valid numer 1-9. ")
           continue


       getpo(play)


       if getpo(play) != None:
           col, row = getpo(play)
           if board[row][col] == " ":
               board[row][col] = symbol
               displayboard()
               playernum += 1
           else:
               print("Cannot place marker there. ")
          


       else:
           print("Please enter a valid numer 1-9. ")


       check_win(board, symbol)


       if check_win(board, symbol):
           print(f'Player {(playernum + 1) % 2 + 1} wins! ')
           win = True
           break


       filled = True
       for r in range(3):
           for c in range(3):
               if board[r][c] == " ":
                   filled = False
       if filled and not win:
           print("Draw! ")
           break


      


tictactoe()

