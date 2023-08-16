from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile, askopenfile

file_name = NONE
def new_file():
    global file_name
    file_name = 'Без названия'
    text.delete('1.0', END)

def open_file():
    global file_name
    file_open = askopenfile(mode='r')
    if file_open is None:
        return
    file_name = file_open.name
    data = file_open.read()
    text.delete('1.0', END)
    text.insert('1.0', data)

def save_as():
    file_save = asksaveasfile(mode='w', defaultextension='.txt')
    data = text.get('1.0', END)
    try:
        file_save.write(data.rstrip())
    except Exception:
        messagebox.showerror('Файл не сохранен')

root = Tk()
root.title('Заметки')
root.geometry('400x400')

text = Text(root, width=400, height=400)
text.pack()

menu_bar = Menu(root)
file_menu = Menu(menu_bar)

file_menu.add_command(label="Новая заметка", command=new_file)
file_menu.add_command(label="Открыть", command=open_file)
file_menu.add_command(label='Сохранить как', command=save_as)

menu_bar.add_cascade(label='Файл', menu=file_menu)

root.config(menu=menu_bar)
root.mainloop()