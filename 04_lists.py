### List ###
my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]
print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, 'Jairo', 'Vega']

print(type(my_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_list.count(30)) # cuenta el número de ocurrencias que tiene una lista
#print(my_other_list[4]) IndexError
#print(my_other_list[-5]) IndexError

""" age, height, name, surname = my_other_list
print(name) """

print(my_list + my_other_list)

my_other_list.append('jairodv')
print(my_other_list)

my_other_list.insert(1, 'rojo')
print(my_other_list)

my_other_list[1] = 'azul'
print(my_other_list)

my_other_list.remove('azul')
print(my_other_list)

my_list.remove(30)
print(my_list)

print(my_list.pop())
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[2]
print(my_list)

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

print(my_new_list[1:3])