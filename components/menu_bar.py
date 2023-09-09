from tkinter import *

class MenuBar: 
    def __init__(self, parent):
        self.parent = parent
        self.menu_bar = Menu(self.parent)
        self.parent.config(menu=self.menu_bar)
        self.debug_mode = False
        self.create_file_menu()
 

    def create_file_menu(self):
        file_menu = Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="Salir", command=self.parent.quit)
        self.menu_bar.add_cascade(label="Archivo", menu=file_menu)

