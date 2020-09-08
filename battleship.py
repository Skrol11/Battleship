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

def get_init_ship(board,player1,player2):
    while player1 == True:
        coordinates_1st_player = input("Give the coordinates, Captain")
        coordinate = coordinates_1st_player.split()
        print(coordinate)












if __name__ == "__main__":
    board_player1 = init_board_player1()
    board_player2 = init_board_player2()
    player1 = get_player_1st_name()
    player2 = get_player_2nd_name()
    player_2 = how_started_HUMAN_HUMAN(player1,player2)
    print_board(board_player1,board_player2, player1, player2)
    a = get_init_ship(player1,player2)