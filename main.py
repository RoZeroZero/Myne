import modules.get_versions as get
from tkinter import *
from tkinter import ttk


ui=Tk()

def click(event):
    # button1.configure(bg="black")
    pass


ui.title("Myne")
ui.resizable(False, False)
ui.iconbitmap(default="assets/myne.ico")
ui.attributes("-fullscreen", False)


label1 = Label(ui, text="Myne Minecraft Modpack Loader", font=("assets/minecraft.ttf", 20))  
label1.pack(anchor=NW, padx=5, pady=5)  
button1 = ttk.Button(ui, text="Не нажимать!")  
button1.pack(anchor=SE, padx=5, pady=5)
button1.bind("<ButtonPress>", click)  

ui.mainloop()