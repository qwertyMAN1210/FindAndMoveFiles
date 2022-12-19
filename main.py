from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *

TITLE = 'File transfer'
WIDTH = 500
HEIGHT = 150
BACKGROUND_COLOR = 'purple'
BACKGROUND_TEXT_COLOR = 'white'
START_BUTTON_COLOR = 'green'
SELECT_BUTTON_COLOR = 'yellow'

open_folder = ''
save_folder = ''


def select_open_folder():
    global open_folder
    new_dir = askdirectory()
    if new_dir:
        open_label['text'] = open_folder = new_dir


def select_save_folder():
    global save_folder
    new_dir = askdirectory()
    if new_dir:
        save_label['text'] = save_folder = new_dir


def start():
    if open_folder != '' and save_folder != '' and askyesno(title='Message', message='Are you sure??'):
        progress_label['bg'] = 'green'
        progress_label['text'] = 'start'
    else:
        progress_label['bg'] = 'red'
        progress_label['text'] = 'please select directories'


window = Tk()
window.title(TITLE)
window.geometry(f'{WIDTH}x{HEIGHT}')
window.configure(bg=BACKGROUND_COLOR)
open_label = Label(window, text='None', bg=BACKGROUND_COLOR, fg=BACKGROUND_TEXT_COLOR, font=('Arial', 12))
save_label = Label(window, text='None', bg=BACKGROUND_COLOR, fg=BACKGROUND_TEXT_COLOR, font=('Arial', 12))
progress_label = Label(window, text='', bg=BACKGROUND_COLOR, fg=BACKGROUND_TEXT_COLOR, font=('Arial', 12))
open_button = Button(window, text='Open folder', width=10, height=1, command=select_open_folder, bg=SELECT_BUTTON_COLOR,
                     font=('Arial', 10))
save_button = Button(window, text='Save folder', width=10, height=1, command=select_save_folder, bg=SELECT_BUTTON_COLOR,
                     font=('Arial', 10))
start_button = Button(window, text='Start', width=5, height=1, command=start, bg=START_BUTTON_COLOR, font=('Arial', 14))
open_button.place(x=10, y=10)
open_label.place(x=100, y=10)
save_button.place(x=10, y=40)
save_label.place(x=100, y=40)
start_button.place(x=10, y=70)
progress_label.place(relx=0.5, y=130, anchor='center')
window.mainloop()
