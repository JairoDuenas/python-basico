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
mi_cursor.execute("INSERT INTO PRODUCTOS VALUES('BALÓN', 15, 'DEPORTES')")

# 5. Cerrar puntero
mi_conexion.commit()

# 6. Cerrar conexión
mi_conexion.close()