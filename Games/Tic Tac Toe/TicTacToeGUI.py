from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
import os
from PIL import Image, ImageTk
from TicTacToe_library import generate_field, generate_field_2


img = generate_field_2((270, 270))

""" This block of code is written only for path control """
path = os.getcwd()  # current working directory
img_path = os.path.abspath('picture.png')   # path to generated image, that represents game field

""" Saving the image as 'picture.png' """
plt.imsave('picture.png', img, cmap='Greys_r')


""" Show image to control """
plt.imshow(img, cmap='Greys_r')
plt.show()


""" GUI creation section """
window = Tk()
# window.geometry('300x300')
frame = Frame()
label = Label(window, text='I want to set an image there')
label.grid()

im = Image.open('picture.png')
ph = ImageTk.PhotoImage(im)

label_img = Label(window, image=ph)
label_img.grid()

save_button = Button(window, text='Save')
save_button.grid(2)
new_game_button = Button(window, text='New game')
new_game_button.grid()

window.mainloop()

