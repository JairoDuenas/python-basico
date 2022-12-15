mi_diccionario = {'Alemania':'Berlín', 'Francia':'París', 'Reino Unido':'Londres', 'Colombia':'Bogotá', 'edad':35, 25:'igual'}
print(mi_diccionario)
print(mi_diccionario['Colombia'])

mi_diccionario['Italia'] = 'Lisboa' # agregar clave con valor erróneo
print(mi_diccionario)

mi_diccionario['Italia'] = 'Roma' # corregir o reasinar valor
print(mi_diccionario)

del mi_diccionario['Reino Unido'] # eliminar clave:valor
print(mi_diccionario)

mi_lista = ['España', 'Francia', 'Reino unido', 'Alemania']
mi_diccionario2 = {mi_lista[0]:'Madrid', mi_lista[1]:'París', mi_lista[2]:'Londres', mi_lista[3]:'Berlín'}
print(mi_diccionario2)
print(mi_diccionario2['Francia'])

mi_diccionario3 = {23:'Jordan', 'Nombre':'Michael', 'Equipo':'Chicago', 'anillos':{'temporadas':(1991,1992,1993,1996,1997,1998)}}
print(mi_diccionario3)
print(mi_diccionario3.keys())
print(mi_diccionario3.values())
print(len(mi_diccionario3))
print(mi_diccionario3['Equipo'])
print(mi_diccionario3['anillos'])

