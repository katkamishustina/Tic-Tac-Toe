import random
import matplotlib.pyplot as plt
from TicTacToe_library import *

matrix = np.zeros((3, 3))
field = generate_field()


def choose(game_field, choice, ox):
    possible_choices_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if choice in possible_choices_2:
        if choice == 7:
            game_field[0][0] = ox
        elif choice == 8:
            game_field[0][1] = ox
        elif choice == 9:
            game_field[0][2] = ox
        elif choice == 4:
            game_field[1][0] = ox
        elif choice == 5:
            game_field[1][1] = ox
        elif choice == 6:
            game_field[1][2] = ox
        elif choice == 1:
            game_field[2][0] = ox
        elif choice == 2:
            game_field[2][1] = ox
        elif choice == 3:
            game_field[2][2] = ox


def get_user_input(message, acceptable_chars = ['1', '2', '3', '4', '5', '6', '7', '8', '9']):
    """
    Get input from user and correct it.
    :param message: string
    :return:
    """

    user_in = input(message)
    while user_in not in acceptable_chars:
        print('Error, input has more characters than required')
        user_in = input(message)
    user_in = int(user_in)
    return user_in


possible_choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
c_map = 'Greys_r'
while len(possible_choices) != 0:
    user_input = get_user_input('Choose position')
    possible_choices.remove(user_input)
    choose(matrix, user_input, 1)
    go_once(field, user_input, True)

    if len(possible_choices) != 0:
        pc_choice = random.choice(possible_choices)
        possible_choices.remove(pc_choice)
        choose(matrix, pc_choice, 2)
        go_once(field, pc_choice, False)

    # ......................horizontal ...........................
    if matrix[0][0] == 1 and matrix[0][1] == 1 and matrix[0][2] == 1:
        print('3 x in one line! USER WON')
        c_map = 'Greys_r'
        break
    elif matrix[0][0] == 2 and matrix[0][1] == 2 and matrix[0][2] == 2:
        print('3 x in one line! PC WON')
        c_map = 'Greys'
        break
    elif matrix[1][0] == 1 and matrix[1][1] == 1 and matrix[1][2] == 1:
        print('3 x in one line! USER WON')
        c_map = 'Greys_r'
        break
    elif matrix[1][0] == 2 and matrix[1][1] == 2 and matrix[1][2] == 2:
        print('3 x in one line! PC WON')
        c_map = 'Greys'
        break
    elif matrix[2][0] == 1 and matrix[2][1] == 1 and matrix[2][2] == 1:
        print('3 x in one line! USER WON')
        c_map = 'Greys_r'
        break
    elif matrix[2][0] == 2 and matrix[2][1] == 2 and matrix[2][2] == 2:
        print('3 x in one line! PC WON')
        c_map = 'Greys'
        break
    # ...................... vertical ...........................
    elif matrix[0][0] == 1 and matrix[1][0] == 1 and matrix[2][0] == 1:
        print('3 x in one line! USER WON')
        c_map = 'Greys_r'
        break
    elif matrix[0][0] == 2 and matrix[1][0] == 2 and matrix[2][0] == 2:
        print('3 x in one line! PC WON')
        c_map = 'Greys'
        break
    elif matrix[0][1] == 1 and matrix[1][1] == 1 and matrix[2][1] == 1:
        print('3 x in one line! USER WON')
        c_map = 'Greys_r'
        break
    elif matrix[0][1] == 2 and matrix[1][1] == 2 and matrix[2][1] == 2:
        print('3 x in one line! PC WON')
        c_map = 'Greys'
        break
    elif matrix[0][2] == 1 and matrix[1][2] == 1 and matrix[2][2] == 1:
        print('3 x in one line! USER WON')
        c_map = 'Greys_r'
        break
    elif matrix[0][2] == 2 and matrix[1][2] == 2 and matrix[2][2] == 2:
        print('3 x in one line! PC WON')
        c_map = 'Greys'
        break

    # ...................... diagonal ...........................
    elif matrix[0][0] == 1 and matrix[1][1] == 1 and matrix[2][2] == 1:
        print('3 x in one line! USER WON')
        c_map = 'Greys_r'
        break
    elif matrix[0][0] == 2 and matrix[1][1] == 2 and matrix[2][2] == 2:
        print('3 x in one line! PC WON')
        c_map = 'Greys'
        break
    elif matrix[0][2] == 1 and matrix[1][1] == 1 and matrix[2][0] == 1:
        print('3 x in one line! USER WON')
        c_map = 'Greys_r'
        break
    elif matrix[0][2] == 2 and matrix[1][1] == 2 and matrix[2][0] == 2:
        print('3 x in one line! PC WON')
        c_map = 'Greys'
        break
    # ................................................................

    plt.imshow(field)
    plt.show()

plt.imshow(field, cmap=c_map)
plt.show()
