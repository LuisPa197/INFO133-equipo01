import csv
import pymysql

# Configuración de la conexión a la base de datos
host = 'localhost'
user = 'root'
password = 'info10000'
database = 'datosComunales'
port = 3306

# Configuración del archivo CSV
csv_file = 'ids.csv'
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
            INSERT INTO comuna (idConectividad,idSeguridad)
            VALUES (%s,%s)
            '''

            for row in csv_data:
                # Ejecutar la consulta de inserción con los datos de cada fila
                cursor.execute(insert_query, tuple(row))

        # Confirmar los cambios en la base de datos
        connection.commit()

        print('Datos cargados correctamente.')
finally:
    # Cerrar la conexión a la base de datos
    connection.close()
