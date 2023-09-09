import tkinter as tk
from ping_handler import PingHandler
from datetime import datetime
from components.menu_bar import MenuBar

class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720")
        self.root.resizable(True, True)
        #menu bar
        self.menu_bar = MenuBar(self.root)

        
        
        """ self.text_widget = tk.Text(root, height=10, width=50)
        self.text_widget.pack()
        self.ping_handler = PingHandler("www.google.com", self)
        self.ping_handler.init_thread_ping()
        self.update_text(["Iniciando..."]) """

    def toggle_debug(self):
        self.debug_mode = not self.debug_mode

    def update_text(self, lineas_tiempo):
        self.text_widget.delete(1.0, tk.END)

        fecha_actual = datetime.now().strftime("%Y_%m_%d")

        nombre_archivo = f"log_{fecha_actual}.txt"

        with open(nombre_archivo, "a") as log_file:
            pass

        with open(nombre_archivo, "r") as log_file:
            all_lines_log = log_file.readlines()
            if len(all_lines_log) > 0 and 'DESCONECTADO' in all_lines_log[-1] and 'DESCONECTADO' in  lineas_tiempo[-1]:
                return
        
        with open(nombre_archivo, "a") as log_file:
            for linea in lineas_tiempo:
                self.text_widget.insert(tk.END, linea + '\n')
                log_file.write(linea + "-----[fecha: " + fecha_actual + "  hora: " + datetime.now().strftime("%H:%M:%S") + "]\n")

        
