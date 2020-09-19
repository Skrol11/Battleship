#1 def init_board(board) 5x5 lista list
#2 print boarda col and row 

#3 Rozmieszczanie statków po boardzie
#while
# get_init_ship sprawdza poprawność wpisania col and row isalpha isnumeric, " ", input result
    # jeżeli jest to nadpisujemy boarda X
    #       def can_init_ship() --> return TRUE na start, sprawdzanie czy mozna postawic statek
    #       A1 --> X board[result[0]][result[1]]
    # jeżeli nie to zwraca nam 3 
#4 def can_init_ship()
#5 print_board(board)
#6 move #3, move #4, move #5

#7 start_game()
#8 shooting_phase():
    #sprawdzanie czy ktoś trafił czy nie
    #   jeżeli tak to nadpisujemy boarda H
        # jeżeli zatopił S
    #   jeżeli nie trafił to M
#9 has_won() True or False
#10 print_board()
#11 Zapętlić program aż ktoś wygra
#12 Opcjonajlnie menu dla 1vs1 lub 1vs AI

import random
import os

clear = lambda: os.system('cls')

ROWS = ['A', 'B', 'C', 'D', 'E']
COLS = ["1","2","3","4","5"]

def get_board():

    board =             [["0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0"]]


    return board

def get_shooting_board():

    board =             [[".", ".", ".", ".", "."],
                        [".", ".", ".", ".", "."],
                        [".", ".", ".", ".", "."],
                        [".", ".", ".", ".", "."],
                        [".", ".", ".", ".", "."]]


    return board

def get_player_name(number):
    player = input("Player what is your name: ")
    print(f"The player is: {player}\n")
    return player


def how_started_HUMAN_HUMAN(player1, player2):
    players = [player1, player2]
    players_2 = random.choice(players)
    print(f"The setting up of ships starts: {players_2}")
    print("")
    input("\n\nTo move on, press the Enter key.")
    return players_2


def how_started_HUMAN_AI(player1):
    print("Computers have more power than humans, so they start")
    input("\n\nTo move on, press the Enter key.")


def print_board(board_player1, board_player2, player1, players_2):

    print("")
    print(f"""   {players_2}                    {player1}""")
    print("")
    print("""  1 2 3 4 5                  1 2 3 4 5""")
    print(f'A {board_player1[0][0]} {board_player1[0][1]} {board_player1[0][2]} {board_player1[0][3]} {board_player1[0][4]}                A {board_player2[0][0]} {board_player2[0][1]} {board_player2[0][2]} {board_player2[0][3]} {board_player2[0][4]}')

    print(f'B {board_player1[1][0]} {board_player1[1][1]} {board_player1[1][2]} {board_player1[1][3]} {board_player1[1][4]}                B {board_player2[1][0]} {board_player2[1][1]} {board_player2[1][2]} {board_player2[1][3]} {board_player2[1][4]}')

    print(f'C {board_player1[2][0]} {board_player1[2][1]} {board_player1[2][2]} {board_player1[2][3]} {board_player1[2][4]}                C {board_player2[2][0]} {board_player2[2][1]} {board_player2[2][2]} {board_player2[2][3]} {board_player2[2][4]}')

    print(f'D {board_player1[3][0]} {board_player1[3][1]} {board_player1[3][2]} {board_player1[3][3]} {board_player1[3][4]}                D {board_player2[3][0]} {board_player2[3][1]} {board_player2[3][2]} {board_player2[3][3]} {board_player2[3][4]}')

    print(f'E {board_player1[4][0]} {board_player1[4][1]} {board_player1[4][2]} {board_player1[4][3]} {board_player1[4][4]}                E {board_player2[4][0]} {board_player2[4][1]} {board_player2[4][2]} {board_player2[4][3]} {board_player2[4][4]}')
    print("")

    input("\n\nTo move on, press the Enter key.")


def one_player_board(board, player1):

    print("")
    print(f"""   {player1}             """)
    print("")
    print("""  1 2 3 4 5               """)
    print(
        f'A {board[0][0]} {board[0][1]} {board[0][2]} {board[0][3]} {board[0][4]} ')

    print(
        f'B {board[1][0]} {board[1][1]} {board[1][2]} {board[1][3]} {board[1][4]} ')

    print(
        f'C {board[2][0]} {board[2][1]} {board[2][2]} {board[2][3]} {board[2][4]}  ')

    print(
        f'D {board[3][0]} {board[3][1]} {board[3][2]} {board[3][3]} {board[3][4]} ')

    print(
        f'E {board[4][0]} {board[4][1]} {board[4][2]} {board[4][3]} {board[4][4]} ')
    print("")

    input("\n\nTo move on, press the Enter key.")


def get_init_ship(board, player):
    while is_init(board):
        ask_1 = input(
            "Czy chcesz postawić:'1-jednomasztowiec' czy '2-masztowiec'")
        if ask_1 == "1":
            row, col = get_coordinates()

            board[row][col] = "X"
            one_player_board(board, player)
            zaznaczanie_sasiadow(board, [row, col])
            
        else:
            row, col = get_coordinates()
            board[row][col] = "X"
            one_player_board(board, player)
            zaznaczanie_sasiadow(board, [row, col])
            
            row2, col2 = get_coordinates()
            while not validate_coordinate(row, col, row2, col2):
                row2, col2 = get_coordinates()
            board[row2][col2] = "X"
            one_player_board(board, player)
            zaznaczanie_sasiadow(board, [row, col])
            zaznaczanie_sasiadow(board, [row2, col2])

    return board

def zaznaczanie_sasiadow(board, a):

    if 0 <= a[0]-1 and board[a[0]-1][a[1]] == "0" :
        board[a[0]-1][a[1]] = "~"
        
    if 4 >= a[0]+1  and board[a[0]+1][a[1]] == "0":
        board[a[0]+1][a[1]] = "~"
        
    if 0 <= a[1]-1 and board[a[0]][a[1]-1] == "0":
        board[a[0]][a[1]-1] = "~"
        
    if 4 >= a[1]+1  and board[a[0]][a[1]+1] == "0":
        board[a[0]][a[1]+1] = "~" 
    print(board)

def validate_coordinate(row, col, row2, col2):
    return row - 1 <= row2 <= row + 1 and col - 1 <= col2 <= col + 1 and not (row2 -1  == row  and col2 - 1 == col) and not (row2 -1 == row and col2 +1 == col) and not (row2 +1 == row and col2 - 1 == col) and not (row2 +1 == row and col2 +1 == col)

def get_coordinates():
    while True:
        coordinates_player = input("Give the coordinates, Captain: ")
        if len(coordinates_player) >= 2:
            row = coordinates_player[0]
            col = coordinates_player[1]
            row = row.upper()
            if row in ROWS and col in COLS:
                row = ROWS.index(row)
                col = int(coordinates_player[1])-1
                return row, col
            else:
                print("Wrong coordinates")
        else:
            print("Good coordinates : 'A1'")
    
def is_init(board):
    counter = 0
    for i in board:
        for j in i:
            if j == "X":
                counter += 1
    return not counter == 2


def play(board_player1, board_player2):
    shot_board_player1 = get_shooting_board()
    shot_board_player2 = get_shooting_board()
    current_board_player = board_player2
    current_shot_board_player = shot_board_player1
    current_player = 1
    
    while not has_won(board_player1, shot_board_player1 ) and not has_won(board_player2, shot_board_player2):
        
        clear()
        one_player_board(current_shot_board_player, current_player)
        while True:
            row, col = get_coordinates()
            if current_shot_board_player[row][col] == ".":
                break
            else:
                print("Wrong coordinates to shot")
        if current_board_player[row][col] == "X":
            print("You Hit")
            current_shot_board_player[row][col] = "H"
        else:
            print("You miss")
            current_shot_board_player[row][col] = "M"
        input("Press enter to continue")
        if current_player == 1:
            current_player = 2
            current_shot_board_player = shot_board_player2
            current_board_player = board_player1
        else:
            current_board_player = board_player2
            current_shot_board_player = shot_board_player1
            current_player = 1
    print("You win")
            
        
        


def has_won(board_player, shot_board_player):
    counter = 0
    for i in board_player:
        for j in i:
            if j == "X":
                counter += 1
    counter_h = 0
    for i in shot_board_player:
        for j in i:
            if j == "H":
                counter_h += 1
    
    return counter == counter_h



if __name__ == "__main__":
    board_player1 = get_board()
    board_player2 = get_board()
    player1 = get_player_name(1)
    player2 = get_player_name(2)
    player_2 = how_started_HUMAN_HUMAN(player1, player2)
    print_board(board_player1, board_player2, player1, player2)
    board_player1 = get_init_ship(board_player1, player1)
    print("Another player")
    board_player2 = get_init_ship(board_player2, player2)
    print_board(board_player1, board_player2, player1, player2)
    print("Shooting time!!!")
    play(board_player1,board_player2)
    
