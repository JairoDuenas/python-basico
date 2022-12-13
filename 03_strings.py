### Strings ###

my_strings = "Mi String"
my_other_string = "Mi otro String"

print(len(my_strings))
print(len(my_other_string))

print(my_strings, my_other_string)
my_new_line_string = "Este es un String \n con salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un string con tabulación"
print(my_tab_string)

my_scape_string = "\t Este es un String \n escapado"
print(my_scape_string)

# Formateo

name, surname = "Jairo", "Dueñas"
print("Mi nombre es Jairo Dueñas")
print(f"Mi nombre es {name} y mi apellido es {surname}")

# Desempaquetado de caracteres
language = 'Python'
a, b, c, d, e, f = language
print(a)
print(e)

# División
language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print('language[0:6:2]', language_slice)

# Reverse
reversed_language = language[::-1]
print(reversed_language)

# Funciones con strings
print(language.capitalize())
print(language.upper())
print(language.count('t'))
print(language.isnumeric())
print(language.lower())
print(language.lower().isupper())
print(language.startswith('py'))
