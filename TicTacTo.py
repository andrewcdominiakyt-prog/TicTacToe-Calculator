player1 = "X"
player2 = "O"

rounds = 0

one_one = "#" 
one_two = "#"  
one_three = "#" 
two_one = "#"
two_two = "#"
two_three = "#"
three_one = "#"
three_two = "#"
three_three = "#"

player1_turn = True
player2_turn = False

gamerunning= False


board = [[one_one, one_two, one_three],
         [two_one, two_two, two_three],
         [three_one, three_two, three_three]]


def gamewin():
    # rows
    for r in range(3):
        if board[r][0] == board[r][1] == board[r][2] != "#":
            print_board(); print(("P1" if board[r][0]=="X" else "P2")+" WINS")
            return True
    # cols
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] != "#":
            print_board(); print(("P1" if board[0][c]=="X" else "P2")+" WINS")
            return True
    # diagonals
    if board[0][0] == board[1][1] == board[2][2] != "#":
        print_board(); print(("P1" if board[0][0]=="X" else "P2")+" WINS")
        return True
    if board[0][2] == board[1][1] == board[2][0] != "#":
        print_board(); print(("P1" if board[0][2]=="X" else "P2")+" WINS")
        return True
    return False

def print_board():
    for row in board:
        print(row[0], row[1], row[2])

        # remember to switch the inputs to calculator positions after finishing the game

def player1turn():  
    global rounds
    if player1_turn == True: 
        while True:
            print_board()
            player1_input = input("P1 SELECT A SPACE (1-9): ")
            if player1_input == "7":
                if board[0][0] == "X" or board[0][0] == "O":
                    print("square taken, pick again")
                    continue
                board[0][0] = "X"
                break
            elif player1_input == "8":
                if board[0][1] == "X" or board[0][1] == "O":
                    print("square taken, pick again")
                    continue
                board[0][1] = "X"
                break
            elif player1_input == "9":
                if board[0][2] == "X" or board[0][2] == "O":
                    print("square taken, pick again")
                    continue
                board[0][2] = "X"
                break
            elif player1_input == "4":
                if board[1][0] == "X" or board[1][0] == "O":
                    print("square taken, pick again")
                    continue
                board[1][0] = "X"
                break
            elif player1_input == "5":
                if board[1][1] == "X" or board[1][1] == "O":
                    print("square taken, pick again")
                    continue
                board[1][1] = "X"
                break
            elif player1_input == "6":
                if board[1][2] == "X" or board[1][2] == "O":
                    print("square taken, pick again")
                    continue
                board[1][2] = "X"
                break
            elif player1_input == "1":
                if board[2][0] == "X" or board[2][0] == "O":
                    print("square taken, pick again")
                    continue
                board[2][0] = "X"
                break
            elif player1_input == "2":
                if board[2][1] == "X" or board[2][1] == "O":
                    print("square taken, pick again")
                    continue
                board[2][1] = "X"
                break
            elif player1_input == "3":
                if board[2][2] == "X" or board[2][2] == "O":
                    print("square taken, pick again")
                    continue
                board[2][2] = "X"
                break
            else:
                print("invalid input")
                continue
            break
        rounds += 1

    
def player2turn():  
    global rounds
    if player2_turn == True: 
        while True:
            print_board()
            player2_input = input("P2 SELECT A SPACE (1-9): ")
            if player2_input == "7":
                if board[0][0] == "X" or board[0][0] == "O":
                    print("square taken, pick again")
                    continue
                board[0][0] = "O"
                break
            elif player2_input == "8":
                if board[0][1] == "X" or board[0][1] == "O":
                    print("square taken, pick again")
                    continue
                board[0][1] = "O"
                break
            elif player2_input == "9":
                if board[0][2] == "X" or board[0][2] == "O":
                    print("square taken, pick again")
                    continue
                board[0][2] = "O"
                break
            elif player2_input == "4":
                if board[1][0] == "X" or board[1][0] == "O":
                    print("square taken, pick again")
                    continue
                board[1][0] = "O"
                break
            elif player2_input == "5":
                if board[1][1] == "X" or board[1][1] == "O":
                    print("square taken, pick again")
                    continue
                board[1][1] = "O"
                break
            elif player2_input == "6":
                if board[1][2] == "X" or board[1][2] == "O":
                    print("square taken, pick again")
                    continue
                board[1][2] = "O"
                break
            elif player2_input == "1":
                if board[2][0] == "X" or board[2][0] == "O":
                    print("square taken, pick again")
                    continue
                board[2][0] = "O"
                break
            elif player2_input == "2":
                if board[2][1] == "X" or board[2][1] == "O":
                    print("square taken, pick again")
                    continue
                board[2][1] = "O"
                break
            elif player2_input == "3":
                if board[2][2] == "X" or board[2][2] == "O":
                    print("square taken, pick again")
                    continue
                board[2][2] = "O"
                break
            else:
                print("invalid input")
                continue
            break
        rounds += 1


gamerunning = True

while gamerunning:
    if gamewin():
        break
    if rounds == 9:
        print("BOARD FULL GAME OVER")
        print_board()
        break
    if player1_turn:
        player1turn()
        player1_turn = False
        player2_turn = True
    elif player2_turn:
        player2turn()
        player2_turn = False
        player1_turn = True
    else:
        print("error")
        break
