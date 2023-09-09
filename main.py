import tkinter as tk
from gui import App
""" import speedtest """

def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()


    """ st = speedtest.Speedtest()
    print("Realizando prueba de velocidad...")


    download_speed = st.download() / 1_000_000
    upload_speed = st.upload() / 1_000_000

    print(f"Velocidad de descarga: {download_speed:.2f} Mbps")
    print(f"Velocidad de carga: {upload_speed:.2f} Mbps")
 """