# import re

# if __name__ == "__main__":
#   print('''  ----------------------
#   Let's play Py-Pac-Poe!
#   ----------------------''')

# start_game = input('Enter start to begin game: ').lower()


# the_board = {'A': 'A', 'B': 'B', 'C': 'C',
#             '1': '1)', 'A1': ' ', 'B1': ' ', 'C1': ' ',
#             '2': '2)', 'A2': ' ', 'B2': ' ', 'C2': ' ',
#             '3': '3)', 'A3': ' ', 'B3': ' ', 'C3': ' '}


# def draw_board(board):
#   print('   ' + board['A'] + '    ' + board['B'] + '    ' + board['C'])
#   print(board['1'] + '  ' + board['A1'] + ' | ' + board['B1'] + ' | ' + board['C1'])
#   print("   -----------")
#   print(board['2'] + '  ' + board['A2'] + ' | ' + board['B2'] + ' | ' + board['C2'])
#   print("   -----------")
#   print(board['3'] + '  ' + board['A3'] + ' | ' + board['B3'] + ' | ' + board['C3'])


# def init_game():

#   turn = 'X'
#   count_turns = 0

#   for i in range(9):
#     draw_board(the_board)

#     move = input("Player " + turn + "'s Move (example B2): ").upper()

#     # Check for valid move (RegEx)
#     if the_board[move] != r'(/[A-C][1-3]\d?/)':
#       the_board[move] = turn
#       count_turns += 1
#     else:
#       print("Bogus move! Please try again... \nPlayer " + turn + "'s Move (example b2):")
#       continue

#     # Check for wins (must be over 5 moves)
#     if count_turns >= 5:
#       # check across 1
#       if the_board['A1'] == the_board['B1'] == the_board['C1'] != ' ':
#         draw_board(the_board)
#         print("Player " + turn + " wins the game!")
#         break
#       # check across 2
#       elif the_board['A2'] == the_board['B2'] == the_board['C2'] != ' ':
#         draw_board(the_board)
#         print("Player " + turn + " wins the game!")
#         break
#       # check across 3
#       elif the_board['A3'] == the_board['B3'] == the_board['C3'] != ' ':
#         draw_board(the_board)
#         print("Player " + turn + " wins the game!")
#         break
#       # check down A
#       elif the_board['A1'] == the_board['A2'] == the_board['A3'] != ' ':
#         draw_board(the_board)
#         print("Player " + turn + " wins the game!")
#         break
#       # check down B
#       elif the_board['B1'] == the_board['B2'] == the_board['B3'] != ' ':
#         draw_board(the_board)
#         print("Player " + turn + " wins the game!")
#         break
#       # check down C
#       elif the_board['C1'] == the_board['C2'] == the_board['C3'] != ' ':
#         draw_board(the_board)
#         print("Player " + turn + " wins the game!")
#         break
#       # check diagonal A1-C3
#       elif the_board['A1'] == the_board['B2'] == the_board['C3'] != ' ':
#         draw_board(the_board)
#         print("Player " + turn + " wins the game!")
#         break
#       # check diagonal C1-A3
#       elif the_board['A3'] == the_board['B2'] == the_board['C1'] != ' ':
#         draw_board(the_board)
#         print("Player " + turn + " wins the game!")
#         break

#     # if the board is full and there are no wins... declare a tie
#     if count_turns == 9:
#       print("Cat's game!")

#     # Change player after every move
#     if turn == 'X':
#       turn = 'O'
#     else:
#       turn = 'X'


# if start_game == 'start':
#   init_game()


# Py-Pac-Poe
print("----------------------")
print("Let's play Py-Pac-Poe!")
print("----------------------")

# global variables
state = {}


# initialize game
def init_game():
    state['board'] = {
        'a1': None, 'b1': None, 'c1': None,
        'a2': None, 'b2': None, 'c2': None,
        'a3': None, 'b3': None, 'c3': None
    }


state['turn'] = 'X'
state['winner'] = None
init_game()


def print_board():
    b = state['board']
    print(
        """
        A   B   C
    1)  {} | {} | {}
        ----------
    2)  {} | {} | {}
        ----------
    3)  {} | {} | {}
    """.format(
            str(b['a1'] or ' '),
            str(b['b1'] or ' '),
            str(b['c1'] or ' '),
            str(b['a2'] or ' '),
            str(b['b2'] or ' '),
            str(b['c2'] or ' '),
            str(b['a3'] or ' '),
            str(b['b3'] or ' '),
            str(b['c3'] or ' ')
        )
    )


print_board()


def get_move():
    move = input(f"Player {state['turn']}'s turn (example A1): ").lower()

    if move in state['board'] and state['board'].get(move) is None:
        return move

def get_winner():
    b = state['board']
    winning_combinations = [
        ['a1', 'b1', 'c1'], ['a2', 'b2', 'c2'], ['a3', 'b3', 'c3'],  # Horizontal
        ['a1', 'b2', 'a3'], ['b1', 'b2', 'b3'], ['c1', 'c2', 'c3'],  # Vertical
        ['a1', 'b2', 'c3'], ['c1', 'b2', 'a3']  # Diagonal
    ]
    for combination in winning_combinations:
        if all(b[element] == b[combination[0]] for element in combination):
            return b[combination[0]]
    if None in b.values():
      return 'T'
    return None

def play_game():
    while state['winner'] is None:
        move = get_move()
        if move:
            state['board'][move] = state['turn']
            print_board()

            winner = get_winner()
            if winner:
                if winner == 'T':
                    print("It's a tie!")
                else:
                    print(f"Player {winner} wins the game!")
                break
            
            state['turn'] = 'O' if state['turn'] == 'X' else 'X'
        else:
            print('Invalid move. Try Again!')


play_game()
