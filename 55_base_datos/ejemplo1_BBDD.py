import sqlite3

# 1. Abrir - crear conexión
mi_conexion=sqlite3.connect('Primera_base')

# 2. Crear puntero
mi_cursor=mi_conexion.cursor()

# 3. Ejecutar query(consulta) SQL
#mi_cursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

# 4. Manejar los resultados de la query(consulta)
"""1. Insertar, Leer, Actualizar, Borrar
    (Create, Read, Update, Delete)"""
""" mi_cursor.execute("INSERT INTO PRODUCTOS VALUES('BALÓN', 15, 'DEPORTES')")"""

# ---- insertar varios datos --------------
""" varios_productos=[
    ('Camiseta', 10, 'Deportes'),
    ('Jarrón', 90, 'Cerámica'),
    ('Camión', 20, 'Juguetes'),
]

mi_cursor.executemany('INSERT INTO PRODUCTOS VALUES (?,?,?)', varios_productos)
 """

# ---- ver información de la base de datos --------------
mi_cursor.execute('SELECT * FROM PRODUCTOS')
variosProductos=mi_cursor.fetchall()

for producto in variosProductos:
    #print(producto)
    print('Nombre artículo: ', producto[0], 'Sección: ', producto[2])

# 5. Cerrar puntero
mi_conexion.commit()

# 6. Cerrar conexión
mi_conexion.close()