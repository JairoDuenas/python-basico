### 1. Instalar pyinstaller en MacOS
- Desde la terminal ejecutar
$ pip install pyinstaller
- Dentro de la carpeta del proyecto ejecutar
$ pyinstaller --onefile practica_calculadora.py

- Agregar icono al archivo ejecutable
$ pyinstaller --onefile --ico=./logo.ico practica_calculadora.py