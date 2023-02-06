import re

# --------- función match ------------------
""" nombre1="Sandra López"
nombre2="Antonio Gómez"
nombre3="María López"

if re.match("Sandra", nombre2, re.IGNORECASE):
  print("Hemos encontrado el nombre")
else:
  print("No lo hemos encontrado") """

cadena1="Jara López"
cadena2="85746345663"
cadena3="a5847746734"

if re.match("\d", cadena2):
  print("Hemos encontrado el número")
else:
  print("No lo hemos encontrado")

# --------- función search ------------------

""" nombre1="Sandra López"
nombre2="Antonio Gómez"
nombre3="María López"

if re.search("López", nombre3, re.IGNORECASE):
  print("Hemos encontrado el nombre")
else:
  print("No lo hemos encontrado") """

codigo1="ldkjdhjskkdjshdh71ldldksjjdhfdj"
codigo2="ldklsjh71ldlsjhfkldlfj"
codigo3="pdpoiejhnhdujkdk"

if re.search("71", codigo3, re.IGNORECASE):
  print("Hemos encontrado el código")
else:
  print("No lo hemos encontrado")