import tkinter
import numpy as np
from matplotlib import pyplot
import os
from TicTacToe_library import generate_field, create_o, create_x, go_once
import random

basic_field = generate_field()

o = create_o()
x = create_x()

basic_field[11:20, 21:30] = x

compare0 = basic_field[1:10, 21:30] == x
compare1 = basic_field[11:20, 21:30] == x
# print(basic_field[11:20, 21:30] == x)
print(False in compare0)
print(False in compare1)

position_idxs = []


pyplot.imshow(basic_field, cmap="Greys_r")
pyplot.show()
