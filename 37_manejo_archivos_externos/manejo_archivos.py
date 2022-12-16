from io import open

### Crear y escribir en el archivo ###
""" archivo_texto = open('archivo.txt', 'w')

frase = 'Estupendo día para estudiar Python \n el viernes'
archivo_texto.write(frase)

archivo_texto.close() """

### Leer el archivo ###
""" archivo_texto = open('archivo.txt', 'r')
texto = archivo_texto.read()
archivo_texto.close()
print(texto) """

### Convertir línea de texto en una lista manipulable ###
""" archivo_texto = open('archivo.txt', 'r')
lineas_texto = archivo_texto.readlines()
archivo_texto.close()
print(lineas_texto)
print(lineas_texto[0])
print(lineas_texto[1]) """

### Agregar más líneas al texto ###
archivo_texto = open('archivo.txt', 'a')
archivo_texto.write('\n siempre es una buena ocación para estudiar Python')
archivo_texto.close()