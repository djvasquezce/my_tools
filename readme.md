1. incluir entornos virtuales
    python -m venv venv
2. activar entorno virtual
    .\venv\Scripts\Activate

    Problemas:  la ejecución de scripts está deshabilitada error
    - Abrir powershell como administrador
    - Ejecutar: Get-ExecutionPolicy
    - Ejectuar: Set-ExecutionPolicy RemoteSigned


4. Para ejecutar el archivo
    python main.py
    python .\main.py

5. Crear ejecutable
(venv) PS C:\Users\danny\OneDrive\Escritorio\Tkinter-app> cd .\executable\
remove all from executable folder (desactivar venv)
(venv) PS C:\Users\danny\OneDrive\Escritorio\Tkinter-app\executable> pyinstaller --onefile ..\main.py 