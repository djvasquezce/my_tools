import subprocess
import re
import time
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
            salida = subprocess.run(comando, capture_output=True, text=True)

            
            lineas_tiempo = re.findall(r'tiempo=\d+ms', salida.stdout)

            #si no hay lineas de tiempo buscar La solicitud de ping no pudo encontrar el host www.google.com. Compruebe el nombre y vuelva a intentarlo."
            if(len(lineas_tiempo) == 0):
                text = re.findall(r'La solicitud de ping', salida.stdout)
                if(len(text) > 0):
                    lineas_tiempo.append("DESCONECTADO TOTALMENTE")

            if(len(lineas_tiempo) == 0):
                text = re.findall(r'Host de destino inaccesible.', salida.stdout)
                if(len(text) > 0):
                    lineas_tiempo.append("DESCONECTADO TOTALMENTE")
                


            for linea in lineas_tiempo:
                print(linea)

            self.app.update_text(lineas_tiempo)

            time.sleep(1)
  
