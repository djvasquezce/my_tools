import subprocess
import re
import time
from datetime import datetime
import threading
class PingHandler:
    def __init__(self, host, app):
        self.app = app
        self.host = host
        self.ping_thread = None

    def init_thread_ping(self):
        if self.ping_thread is None or not self.ping_thread.is_alive():
            self.ping_thread = threading.Thread(target=self.start_ping)
            self.ping_thread.start()

    def start_ping(self):
        while True:
            comando = ["ping", self.host]
            output = subprocess.run(comando, capture_output=True, text=True)
            lineas_tiempo = []

            text = ""
            salida = re.findall(r'tiempo=\d+ms', output.stdout)

            for linea in salida:
                text = linea
                if(int(linea.split('=')[1].replace('ms', '')) > 85):
                    lineas_tiempo.append(linea)

           
            if(len(lineas_tiempo) == 0):
                salida = re.findall(r'La solicitud de ping', output.stdout)
                if(len(salida) > 0):
                    text = "DESCONECTADO TOTALMENTE"
                    lineas_tiempo.append("DESCONECTADO TOTALMENTE")

            if(len(lineas_tiempo) == 0):
                salida = re.findall(r'Tiempo de espera', output.stdout)
                if(len(salida) > 0):
                    text = "Tiempo de espera agotado para esta solicitud"
                    lineas_tiempo.append("Tiempo de espera agotado para esta solicitud")
                

            self.app.update_text(text)
            
            if len(lineas_tiempo) > 0:
                self.save_log_ping(lineas_tiempo)

            time.sleep(1)

    def save_log_ping(self, lineas_tiempo):
        fecha_actual = datetime.now().strftime("%Y_%m_%d")
        nombre_archivo = f"log_{fecha_actual}.log"

        with open(nombre_archivo, "a") as log_file:
            pass

        with open(nombre_archivo, "r") as log_file:
            all_lines_log = log_file.readlines()
            if len(all_lines_log) > 0:
                if 'DESCONECTADO' in all_lines_log[-1] and 'DESCONECTADO' in  lineas_tiempo[-1]:
                    return
                
                print(lineas_tiempo)
                if 'Tiempo de espera' in all_lines_log[-1] and 'Tiempo de espera' in  lineas_tiempo[-1]:
                    return
        
        with open(nombre_archivo, "a") as log_file:
            for linea in lineas_tiempo:
                log_file.write(linea + "-----[fecha: " + fecha_actual + "  hora: " + datetime.now().strftime("%H:%M:%S") + "]\n")
    def stop_thread_ping(self):
        if self.ping_thread is not None and self.ping_thread.is_alive():
            self.ping_thread.join()
            self.ping_thread = None
  
