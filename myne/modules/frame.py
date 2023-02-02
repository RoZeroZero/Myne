from tkinter import *
from main import *
from config import *

ui=Tk()


ui.title("Myne")
ui.resizable(False, False)
ui.geometry(xy)
ui.iconbitmap(default=ico)
ui.attributes("-fullscreen", False)


label_versions = Label(ui, text="Versions", font=(font, 10))  
label_versions.place(x=x_l, y=5)

label_description = Label(ui, text="Description", font=(font, 10))
label_description.place(x=x_r, y=5)

label_nickname = Label(ui, text="Nickname", font=(font, 10))
label_nickname.place(x=x_r, y=185)

label_password = Label(ui, text="Password", font=(font, 10))
label_password.place(x=x_rd, y=185)

listbox_versions = Listbox()
listbox_versions.place(x=x_l, y=25, height=230)

listbox_description = Listbox()
listbox_description.place(x=x_r, y=25, height=150, width=265)

entry_nickname = Entry()
entry_nickname.place(x=x_r, y=205)

entry_password = Entry()
entry_password.place(x=x_rd, y=205, width=100)

entry_path = Entry(font=(font, 8))
entry_path.place(x=x_r, y=235, width=145, height=19)
entry_path.insert(0, "Path")

menu_settings = Menu()
menu_settings.add_command(label="Settings", command=menu_settings_click)

button_work = Button(ui, text="Play", font=(font, 8))
button_work.place(x=325, y=235, height=19, width=100)
button_work.bind("<ButtonPress>", button_work_click)

ui.config(menu=menu_settings)
ui.mainloop()