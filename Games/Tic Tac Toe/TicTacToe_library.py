import numpy as np


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


def create_o():
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


def create_x():
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


def go_once(field, choice, ox):
    if choice == 7:
        if ox:
            field[1:10, 1:10] = create_x()
        else:
            field[1:10, 1:10] = create_o()
    elif choice == 8:
        if ox:
            field[1:10, 11:20] = create_x()
        else:
            field[1:10, 11:20] = create_o()
    if choice == 9:
        if ox:
            field[1:10, 21:30] = create_x()
        else:
            field[1:10, 21:30] = create_o()
    elif choice == 4:
        if ox:
            field[11:20, 1:10] = create_x()
        else:
            field[11:20, 1:10] = create_o()
    if choice == 5:
        if ox:
            field[11:20, 11:20] = create_x()
        else:
            field[11:20, 11:20] = create_o()
    elif choice == 6:
        if ox:
            field[11:20, 21:30] = create_x()
        else:
            field[11:20, 21:30] = create_o()
    if choice == 1:
        if ox:
            field[21:30, 1:10] = create_x()
        else:
            field[21:30, 1:10] = create_o()
    elif choice == 2:
        if ox:
            field[21:30, 11:20] = create_x()
        else:
            field[21:30, 11:20] = create_o()
    elif choice == 3:
        if ox:
            field[21:30, 21:30] = create_x()
        else:
            field[21:30, 21:30] = create_o()


def generate_field_2(field_size):

    field_image = np.zeros(field_size)
    field_image[field_image == 0] = 255

    field_length = field_size[0]
    field_weigth = field_size[1]

    field_image[0:field_weigth//30, ::] = 0
    field_image[::, 0:field_weigth//30] = 0

    field_image[0+field_weigth//3:0+field_weigth//3+field_weigth//30, ::] = 0
    field_image[::, 0+field_weigth//3:0+field_weigth//3+field_weigth//30] = 0

    field_image[0+2*field_weigth//3:0+2*field_weigth//3+field_weigth//30, ::] = 0
    field_image[::, 0+2*field_weigth//3:0+2*field_weigth//3+field_weigth//30] = 0

    field_image[-field_weigth//30:, :] = 0
    field_image[:, -field_weigth//30::] = 0
    return field_image

