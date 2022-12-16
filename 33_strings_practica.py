""" nombre_usuario = input('Ingrese su nombre de usuario: ')

print(f'El nombre es: {nombre_usuario.upper()}')
print(f'El nombre es: {nombre_usuario.lower()}')
print(f'El nombre es: {nombre_usuario.capitalize()}') """

edad =  input('Ingrese la edad: ')

while(edad.isdigit() == False):
  print('Ingrese un valor numérico')
  edad =  input('Ingrese la edad: ')

if (int(edad) < 18):
  print('No puede pasar')
else:
  print('Puedes pasar')

