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

def init_board_player1():
    board_player1 =   [["0","0","0","0","0"],         
                       ["0","0","0","0","0"],
                       ["0","0","0","0","0"],
                       ["0","0","0","0","0"],
                       ["0","0","0","0","0"]]
        
    return board_player1

def init_board_player2():
    board_player2   =   [["0","0","0","0","0"],         
                         ["0","0","0","0","0"],
                         ["0","0","0","0","0"],
                         ["0","0","0","0","0"],
                         ["0","0","0","0","0"]]
        
    return board_player2


def get_player_1st_name():
    player1 = input("Player 1 what is your name: ")
    print(f"The player one is: {player1}\n")
    return player1

def get_player_2nd_name():
    player2 = input("Player 2 what is your name: ")
    print(f"The second player is: {player2}\n")
    return player2

def how_started_HUMAN_HUMAN(player1, player2):
    players = [player1,player2]
    players_2 = random.choice(players)
    print(f"The setting up of ships starts: {players_2}")
    print("")
    input("\n\nTo move on, press the Enter key.")
    return players_2

def how_started_HUMAN_AI(player1):
    print("Computers have more power than humans, so they start")
    input("\n\nTo move on, press the Enter key.")


def print_board(board_player1,board_player2, player1, player2):

    print("")
    print(f"""   {player1}                    {player2}""")
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
    print(f'A {board[0][0]} {board[0][1]} {board[0][2]} {board[0][3]} {board[0][4]} ')               

    print(f'B {board[1][0]} {board[1][1]} {board[1][2]} {board[1][3]} {board[1][4]} ')               

    print(f'C {board[2][0]} {board[2][1]} {board[2][2]} {board[2][3]} {board[2][4]}  ')              

    print(f'D {board[3][0]} {board[3][1]} {board[3][2]} {board[3][3]} {board[3][4]} ')               

    print(f'E {board[4][0]} {board[4][1]} {board[4][2]} {board[4][3]} {board[4][4]} ')               
    print("")


    input("\n\nTo move on, press the Enter key.")
def get_init_ship(board,player):
    while is_init(board):
        ask_1 = input("Czy chcesz postawić jednomasztowiec: '1-jednomasztowiec'/'2-masztowiec'")
        if ask_1 == "1":
            coordinates_player = input("Give the coordinates, Captain: ")
            row = coordinates_player[0]
            row = row.upper()
            if row.isalpha():
                if row == "A":
                    row = 0
                elif row == "B":
                    row = 1
                elif row == "C":
                    row = 2
                elif row == "D":
                    row = 3
                elif row == "E":
                    row = 4
            col = int(coordinates_player[1])-1
            board[row][col] = "X"
            one_player_board(board, player)
        else:
            #Podwójny input dla dwumasztowca
            coordinates_player = input("Give the coordinates, Captain: ")
            row = coordinates_player[0]
            row = row.upper()
            if row.isalpha():
                if row == "A":
                    row = 0
                elif row == "B":
                    row = 1
                elif row == "C":
                    row = 2
                elif row == "D":
                    row = 3
                elif row == "E":
                    row = 4
            col = int(coordinates_player[1])-1
            board[row][col] = "X"
            one_player_board(board, player)

    return board



    while is_init(board):
        coordinates_player = input("Give the coordinates, Captain: ")
        row = coordinates_player[0]
        row = row.upper()
        if row.isalpha():
            if row == "A":
                row = 0
            elif row == "B":
                row = 1
            elif row == "C":
                row = 2
            elif row == "D":
                row = 3
            elif row == "E":
                row = 4
        col = int(coordinates_player[1])-1
        board[row][col] = "X"
        one_player_board(board, player)
    return board

def is_init(board):
    counter = 0
    for i in board:
        for j in i:
            if j == "X":
                counter += 1
    if counter == 7:
        return False
    else:
        return True















if __name__ == "__main__":
    board_player1 = init_board_player1()
    board_player2 = init_board_player2()
    player1 = get_player_1st_name()
    player2 = get_player_2nd_name()
    player_2 = how_started_HUMAN_HUMAN(player1,player2)
    print_board(board_player1,board_player2, player1, player2)
    board_player1 = get_init_ship(board_player1,player1)
    print("Another player")
    board_player2 =  get_init_ship(board_player2,player2)
    print_board(board_player1,board_player2, player1, player2)