import csv
import pymysql

# Configuración de la conexión a la base de datos
host = 'localhost'
user = 'root'
password = 'info10000'
database = 'datosComunales'
port = 3306

# Configuración del archivo CSV
csv_file = 'comunas2.csv'
delimiter = ';'

# Establecer la conexión a la base de datos
connection = pymysql.connect(host=host, user=user, password=password, database=database, port=port)

try:
    with connection.cursor() as cursor:

        # Abrir el archivo CSV y cargar los datos a la base de datos
        with open(csv_file, 'r') as file:
            csv_data = csv.reader(file, delimiter=delimiter)
            header = next(csv_data)  # Leer la primera línea del archivo CSV (encabezados de columna)

            # Crear la consulta de inserción de datos
            insert_query = '''
            INSERT INTO comuna (idComuna,nombre,poblacion,superficie,viviendas,idRegion)
            VALUES (%s,%s,%s,%s,%s,%s)
            '''

            for row in csv_data:
                # Ejecutar la consulta de inserción con los datos de cada fila
                cursor.execute(insert_query, tuple(row))

        # Confirmar los cambios en la base de datos
        connection.commit()
        print('Datos de comunas cargados correctamente.')

        #cambiar al siguente csv
        csv_file = 'centrosalud.csv'
        
        with open(csv_file, 'r') as file:
            csv_data = csv.reader(file, delimiter=delimiter)
            header = next(csv_data)  # Leer la primera línea del archivo CSV (encabezados de columna)

            # Crear la consulta de inserción de datos
            insert_query = '''
            INSERT INTO centroSalud (idCentro,nombre,direccion,telefono,idComuna)
            VALUES (%s,%s,%s,%s,%s)
            '''

            for row in csv_data:
                # Ejecutar la consulta de inserción con los datos de cada fila
                cursor.execute(insert_query, tuple(row))

        # Confirmar los cambios en la base de datos
        connection.commit()

        print('Datos centros de salud cargados correctamente.')


        #cambiar al siguente csv
        csv_file = 'conectividad.csv'
        
        with open(csv_file, 'r') as file:
            csv_data = csv.reader(file, delimiter=delimiter)
            header = next(csv_data)  # Leer la primera línea del archivo CSV (encabezados de columna)

            # Crear la consulta de inserción de datos
            insert_query = '''
            INSERT INTO conectividad (idConectividad,conexionesInternet,idComuna)
            VALUES (%s,%s,%s)
            '''

            for row in csv_data:
                # Ejecutar la consulta de inserción con los datos de cada fila
                cursor.execute(insert_query, tuple(row))

        # Confirmar los cambios en la base de datos
        connection.commit()

        print('Datos de conectividad cargados correctamente.')

        #cambiar al siguente csv
        csv_file = 'educacion.csv'
        
        with open(csv_file, 'r') as file:
            csv_data = csv.reader(file, delimiter=delimiter)
            header = next(csv_data)  # Leer la primera línea del archivo CSV (encabezados de columna)

            # Crear la consulta de inserción de datos
            insert_query = '''
            INSERT INTO establecimientoEducacion (idEstablecimiento,nombre,PACE,idComuna)
            VALUES (%s,%s,%s,%s)
            '''

            for row in csv_data:
                # Ejecutar la consulta de inserción con los datos de cada fila
                cursor.execute(insert_query, tuple(row))

        # Confirmar los cambios en la base de datos
        connection.commit()

        print('Datos de educacion cargados correctamente.')

        #cambiar al siguente csv
        csv_file = 'seguridad1.csv'
        
        with open(csv_file, 'r') as file:
            csv_data = csv.reader(file, delimiter=delimiter)
            header = next(csv_data)  # Leer la primera línea del archivo CSV (encabezados de columna)

            # Crear la consulta de inserción de datos
            insert_query = '''
            INSERT INTO seguridad (idSeguridad,tasaDenunciasDMCS,indiceVulnerabilidad,idComuna)
            VALUES (%s,%s,%s,%s)
            '''

            for row in csv_data:
                # Ejecutar la consulta de inserción con los datos de cada fila
                cursor.execute(insert_query, tuple(row))

        # Confirmar los cambios en la base de datos
        connection.commit()

        print('Datos de seguridad cargados correctamente.')        

finally:
    # Cerrar la conexión a la base de datos
    connection.close()
print('Fin del programa de carga.')