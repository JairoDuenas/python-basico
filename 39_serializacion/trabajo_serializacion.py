import pickle

# Archivo binario
""" lista_nombres = ['Pedro', 'Ana', 'María', 'Isabel']

fichero_binario = open('lista_nombres', 'wb')
pickle.dump(lista_nombres, fichero_binario)
fichero_binario.close()
del (fichero_binario) """

# Rescatando el fichero bianrio

fichero = open('lista_nombres', 'rb')
lista = pickle.load(fichero)
print(lista)

