import re

cadena="Vamos a aprender expresiones regulares en Python. Python es un lenguaje de sintaxix sencilla"
#print(re.search("aprender", cadena))
texto_buscar="aprender"
texto_encontrado=re.search(texto_buscar, cadena)
print(texto_encontrado.start())
print(texto_encontrado.end())
print(texto_encontrado.span())

texto_buscar2="Python"
print(len(re.findall(texto_buscar2, cadena)))

""" if re.search(texto_buscar, cadena) is not None:
  print("He encontrado el texto")
else:
  print("No he encontrado el texto") """



