from tkinter import messagebox
from tkinter import *


def refresh(root):

    btn_settings = Button(root, text='0', width=7, height=1, fg='red', font='arial 10')
    btn_settings.grid(row=1, column=1)
    counter = int(root.btn_settings['text']) + 1
    btn_settings['text'] = str(counter)
    # messagebox.showinfo('Test', 'Testestestestest')
