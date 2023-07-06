import mysql.connector

# Conexión a la base de datos
cnx = mysql.connector.connect(user='root', password='info10000',
                              host='localhost',
                              database='datosComunales')

# Crear un cursor para ejecutar consultas
cursor = cnx.cursor()
stay="y"

while (stay=="y"):
	op=input("opciones:\n1. Densidad Poblacional por región\n 2.\n3. promedio de personas por vivienda \n4.\n5.\n6.\n7.\n8.\n9.\n10.\n11.\n12\n13\n")

	#La primera
	if (op=="1") :
		rer=str(input("De que region desa el listado (formato numero):"))
		consulta1="select r.nombre, c.nombre, c.poblacion, c.superficie, c.poblacion/c.superficie as densidad_poblacional from region r JOIN comuna c ON r.idRegion = c.idRegion WHERE r.idRegion ="+rer+"  order by densidad_poblacional DESC;"
		cursor.execute(consulta1)
		resultados=cursor.fetchall()
		#print("--------------------------------")
		for resultado in resultados:
			comuna= resultado[1]
			densidad= resultado[-1]
			#print("|",comuna,"           |",densidad,"|")
			print("| {:<20} | {:<10} |".format(comuna, densidad))
		#print("--------------------------------")

	if (op=="3") :
		rer=str(input("De que region desea el listado (formato numero):"))
		consulta1="select r.idRegion, r.nombre,  c.nombre, c.poblacion, c.viviendas, c.poblacion/c.viviendas as promedio_personas_por_vivienda from region r JOIN comuna c ON r.idRegion = c.idRegion WHERE r.idRegion ="+rer+"  order by densidad_poblacional DESC;"
		cursor.execute(consulta1)
		resultados=cursor.fetchall()
		#print("--------------------------------")
		for resultado in resultados:
			comuna= resultado[1]
			densidad= resultado[-1]
			#print("|",comuna,"           |",densidad,"|")
			print("| {:<20} | {:<10} |".format(comuna, densidad))

	# Función para ejecutar una consulta SQL
#	def ejecutar_consulta(consulta):
#		try:
#		    cursor.execute(consulta)
#		    resultados = cursor.fetchall()
#		    return resultados
#		except mysql.connector.Error as err:
#		    print("Error en la consulta: {}".format(err))
#
	# Solicitar consulta al usuario
#	consulta_usuario = input("Introduce tu consulta SQL: ")

	# Ejecutar la consulta y mostrar los resultados
#	resultados = ejecutar_consulta(consulta_usuario)
#
#	if resultados:
#		for resultado in resultados:
#		    print(resultado)
#	else:
#		print("No se encontraron resultados.")

	# Cerrar el cursor y la conexión a la base de datos """
	stay=input("Desea realizar otra consulta y/n?:")
cursor.close()
cnx.close()

