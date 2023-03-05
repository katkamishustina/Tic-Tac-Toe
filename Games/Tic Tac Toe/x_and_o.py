from random import *

import numpy as np
import matplotlib.pyplot as plt


def generate_field():
    field_image = np.zeros((31, 31))
    field_image[field_image == 0] = 255
    field_image[0, ::] = 0
    field_image[-1, ::] = 0
    field_image[::, 0] = 0
    field_image[::, -1] = 0
    field_image[10, ::] = 0
    field_image[20, ::] = 0
    field_image[::, 10] = 0
    field_image[::, 20] = 0
    return field_image


def print_x():
    '''
    function creates x mask
    :return:
    '''
    x = np.zeros((6, 6))
    y = np.zeros((9, 9))
    for i in range(x.shape[0]):
        x[i, i] = 255
        x[i, -i] = 255
    x = x[1:, 1:]
    y[2:-2, 2:-2] += x  # X template created
    x = y
    x[x == 0] = 1
    x[x == 255] = 0
    x[x == 1] = 255
    return x


def print_o():
    '''
    function creates o mask
    :return:
    '''
    x = np.zeros((5, 5))
    y = np.zeros((9, 9))
    x[0, ::] = 255
    x[::, 0] = 255
    x[-1, ::] = 255
    x[::, -1] = 255
    y[2:-2, 2:-2] += x  # X template created
    x = y
    x[x == 0] = 1
    x[x == 255] = 0
    x[x == 1] = 255
    return x


field = generate_field()


def go_once(field, choise, ox):
    if choise == 7:
        if ox == True:
            field[1:10, 1:10] = print_x()
        else:
            field[1:10, 1:10] = print_o()
    elif choise == 8:
        if ox == True:
            field[1:10, 11:20] = print_x()
        else:
            field[1:10, 11:20] = print_o()
    if choise == 9:
        if ox == True:
            field[1:10, 21:30] = print_x()
        else:
            field[1:10, 21:30] = print_o()
    elif choise == 4:
        if ox == True:
            field[11:20, 1:10] = print_x()
        else:
            field[11:20, 1:10] = print_o()
    if choise == 5:
        if ox == True:
            field[11:20, 11:20] = print_x()
        else:
            field[11:20, 11:20] = print_o()
    elif choise == 6:
        if ox == True:
            field[11:20, 21:30] = print_x()
        else:
            field[11:20, 21:30] = print_o()
    if choise == 1:
        if ox == True:
            field[21:30, 1:10] = print_x()
        else:
            field[21:30, 1:10] = print_o()
    elif choise == 2:
        if ox == True:
            field[21:30, 11:20] = print_x()
        else:
            field[21:30, 11:20] = print_o()
    elif choise == 3:
        if ox == True:
            field[21:30, 21:30] = print_x()
        else:
            field[21:30, 21:30] = print_o()


# go_once(field, 5, False)
# go_once(field, 9, True)
# plt.imshow(field, cmap="Greys_r")
# plt.show()
# plt.close()
#
# go_once(field, 7, False)
# go_once(field, 1, True)
# plt.imshow(field, cmap="Greys_r")
# plt.show()
# plt.close()

# choices = []
# possible_choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# while len(choices) != 9:
#     print('Actually used positions:', choices)
#     user_choice = int(input('Choose position'))
#     while user_choice not in possible_choices:
#         print('You have chosen incorrect position, try again.')
#         user_choice = int(input('Choose position'))
#     if user_choice not in choices and user_choice in possible_choices:
#         choices.append(user_choice)
#     else:
#         print('This position is already used, try other')
#         continue


# possible_choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# while len(possible_choices) != 0:
#     print('Free positions:', possible_choices)
#     user_choice = int(input('Choose position'))
#     while user_choice not in possible_choices:
#         print('You have chosen incorrect position, try again.')
#         user_choice = int(input('Choose position'))
#     if user_choice in possible_choices:
#         possible_choices.remove(user_choice)
#     else:
#         print('This position is already used, try other')

def triplet_control():

    ######## x control ##########################
    if print_x() in field[1:10, 1:10]:
        if print_x() in field[11:20, 11:20]:
            if print_x() in field[21:30, 21:30]:
                print('USER WIN!')
                return True

    elif print_x() in field[21:30, 1:10]:
        if print_x() in field[11:20, 11:20]:
            if print_x() in field[1:10, 21:30]:
                print('USER WIN!')
                return True

    elif print_x() in field[21:30, 1:10]:
        if print_x() in field[21:30, 11:21]:
            if print_x() in field[21:30, 21:30]:
                print('USER WIN!')
                return True

    elif print_x() in field[11:21, 1:10]:
        if print_x() in field[11:21, 11:21]:
            if print_x() in field[11:21, 21:30]:
                print('USER WIN!')
                return True

    elif print_x() in field[1:10, 1:10]:
        if print_x() in field[1:10, 11:21]:
            if print_x() in field[1:10, 21:30]:
                print('USER WIN!')
                return True

    elif print_x() in field[1:10, 21:30]:
        if print_x() in field[11:21, 21:30]:
            if print_x() in field[21:30, 21:30]:
                print('USER WIN!')
                return True

    elif print_x() in field[1:10, 11:21]:
        if print_x() in field[11:21, 11:21]:
            if print_x() in field[21:30, 11:21]:
                print('USER WIN!')
                return True

    elif print_x() in field[1:10, 1:10]:
        if print_x() in field[11:21, 1:10]:
            if print_x() in field[21:30, 1:10]:
                print('USER WIN!')
                return True

    ######## o control ##########################

    if print_o() in field[1:10, 1:10]:
        if print_o() in field[11:20, 11:20]:
            if print_o() in field[21:30, 21:30]:
                print('PC WIN!')
                return True

    elif print_o() in field[21:30, 1:10]:
        if print_o() in field[11:20, 11:20]:
            if print_o() in field[1:10, 21:30]:
                print('PC WIN!')
                return True

    elif print_o() in field[21:30, 1:10]:
        if print_o() in field[21:30, 11:21]:
            if print_o() in field[21:30, 21:30]:
                print('PC WIN!')
                return True

    elif print_o() in field[11:21, 1:10]:
        if print_o() in field[11:21, 11:21]:
            if print_o() in field[11:21, 21:30]:
                print('PC WIN!')
                return True

    elif print_o() in field[1:10, 1:10]:
        if print_o() in field[1:10, 11:21]:
            if print_o() in field[1:10, 21:30]:
                print('PC WIN!')
                return True

    elif print_o() in field[1:10, 21:30]:
        if print_o() in field[11:21, 21:30]:
            if print_o() in field[21:30, 21:30]:
                print('PC WIN!')
                return True

    elif print_o() in field[1:10, 11:21]:
        if print_o() in field[11:21, 11:21]:
            if print_o() in field[21:30, 11:21]:
                print('PC WIN!')
                return True

    elif print_o() in field[1:10, 1:10]:
        if print_o() in field[11:21, 1:10]:
            if print_o() in field[21:30, 1:10]:
                print('PC WIN!')
                return True


possible_choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]

while len(possible_choices) != 0:
    print('Free positions:', possible_choices)
    user_choice = int(input('Choose position'))
    while user_choice not in possible_choices:
        print('You have chosen incorrect position, try again.')
        user_choice = int(input('Choose position'))
    if user_choice in possible_choices:
        possible_choices.remove(user_choice)
        if len(possible_choices) != 0:
            pc_choice = choice(possible_choices)
            possible_choices.remove(pc_choice)
            go_once(field, pc_choice, False)
            triplet_control()
        print(f'PC choices')
    else:
        print('This position is already used, try other')
    go_once(field, user_choice, True)
    triplet_control()
    plt.imshow(field, cmap="Greys_r")
    plt.show()



