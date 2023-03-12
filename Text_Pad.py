from tkinter import *
from tkinter.filedialog import asksaveasfilename

file_path = ''

def exit():
    win.destroy()

def set_file_path(path):
    global file_path
    file_path = path

def save_as():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Text Document', '.txt')],
        defaultextension=('.txt'))
    else:
        path = file_path
    with open(path, 'w') as file:
        code = txt.get('1.0', END)
        file.write(code)
        set_file_path(path)

win = Tk()

fileoptions = [
    "Save",
    "Save as",
    "Exit",
]
  
clicked = StringVar()
  
clicked.set( "File" )

menu_bar = Menu(win)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Save', command=save_as)
file_menu.add_command(label='Save As', command=save_as)
file_menu.add_command(label='Exit', command=exit)
menu_bar.add_cascade(label='File', menu=file_menu)

win.config(menu=menu_bar)

txt = Text()
txt.pack()

win.title("Verdazm Textpad")
win.geometry('400x500')
win.mainloop()