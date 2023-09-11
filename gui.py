import tkinter as tk
from ping_handler import PingHandler

class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720")
        self.root.resizable(True, True)
      
        self.text_widget = tk.Text(root, height=5, width=40)
        self.text_widget.grid(row=0, column=0)
        self.button_ping = tk.Button(root, text="Ping", command=self.init_ping)
        self.button_ping.grid(row=1, column=0)
        

    def update_text(self, text):
        self.text_widget.delete(1.0, tk.END)
        self.text_widget.insert(tk.END, text)

    def on_closing(self):
        self.ping_handler.stop_thread_ping()
        self.root.destroy()

    def init_ping(self):
        self.ping_handler = PingHandler("www.google.com", self)
        self.ping_handler.init_thread_ping()
        #disable button
        self.button_ping.config(state=tk.DISABLED)
        
