player1 = "X"
player2 = "O"


one_one = 0
one_two = 0
one_three = 0
two_one = 0
two_two = 0
two_three = 0
three_one = 0
three_two = 0
three_three = 0

player1_turn = True
player2_turn = False


board = [[one_one, one_two, one_three],
         [two_one, two_two, two_three],
         [three_one, three_two, three_three]]

def print_board():
    for row in board:
        print(' '.join([str(cell) for cell in row]))

print_board()

def player1turn():  
    if player1_turn == True: 
        print("player 1 turn")
        player1_input = input("please select a square (1-9): ")
        if player1_input == "1":
            if board[0][0] == "X" or board[0][0] == "O":
                print("square taken, pick again")
            board[0][0] = "X"
        elif player1_input == "2":
            if board[0][1] == "X" or board[0][1] == "O":
                print("square taken, pick again")
            board[0][1] = "X"
        elif player1_input == "3":
            if board[0][2] == "X" or board[0][2] == "O":
                print("square taken, pick again")
            board[0][2] = "X"
        elif player1_input == "4":
            if board[1][0] == "X" or board[1][0] == "O":
                print("square taken, pick again")
            board[1][0] = "X"
        elif player1_input == "5":
            if board[1][1] == "X" or board[1][1] == "O":
                print("square taken, pick again")  
            board[1][1] = "X"
        elif player1_input == "6":
            if board[1][2] == "X" or board[1][2] == "O":
                print("square taken, pick again")
            board[1][2] = "X"
        elif player1_input == "7":
            if board[2][0] == "X" or board[2][0] == "O":
                print("square taken, pick again")
            board[2][0] = "X"
        elif player1_input == "8":
            if board[2][1] == "X" or board[2][1] == "O":
                print("square taken, pick again")
            board[2][1] = "X"
        elif player1_input == "9":
            if board[2][2] == "X" or board[2][2] == "O":
                print("square taken, pick again")
            board[2][2] = "X"
        else:
            print("invalid input")
        print_board()


player1turn()

player1turn()