### Tuples ###

my_tuple = tuple()
my_other_tuple = (35, 24, 50)

my_tuple = (35, 1.77, 'Jairo', 'Vega')
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) IndexError
#print(my_tuple[-6]) IndexError

print(my_tuple.count(35))
print(my_tuple.index('Jairo'))

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple) # convertir una tupla a una lista
print(type(my_tuple))

my_tuple[3] = 'jairodv'
print(my_tuple)
my_tuple.insert(1, 'azul')

my_tuple = tuple(my_tuple) # convertir una lista a una tupla
print(type(my_tuple))


