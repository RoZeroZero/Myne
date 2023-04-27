from tkinter import *
from tkinter import ttk
from main import *
from config import *

ui=Tk()


ui.title('Myne')
ui.resizable(False, False)
ui.geometry(xy)
ui.iconbitmap(default=ico)
ui.attributes('-fullscreen', False)


label_versions = Label(ui, text='Versions', font=(font, 10))  
label_versions.place(x=x_l, y=5)

label_description = Label(ui, text='Description', font=(font, 10))
label_description.place(x=x_r, y=5)

listbox_versions = Listbox(font=(font, 10))
listbox_versions.place(x=x_l, y=25, height=230, width=200)
listbox_versions.bind('<<ListboxSelect>>', listbox_versions_click)

text_description = Text(wrap='word', font=(font, 10))
text_description.place(x=x_r, y=25, height=150, width=265)

entry_path = Entry(font=(font, 8))
entry_path.place(x=x_r, y=235, width=145, height=19)
entry_path.insert(0, minecraft_path)

progressbar = ttk.Progressbar(orient="horizontal")

menu_settings = Menu()
menu_settings.add_command(label='Settings', command=menu_settings_click)

button_work = Button(ui, text='Choose', font=(font, 8), state=["disabled"], command=button_work_click) # type: ignore
button_work.place(x=x_rd, y=235, height=19, width=100)

ui.config(menu=menu_settings)
on_start()
ui.mainloop()