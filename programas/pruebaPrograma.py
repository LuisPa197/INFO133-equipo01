import mysql.connector

# Conexión a la base de datos
cnx = mysql.connector.connect(user='root', password='info10000',
                              host='localhost',
                              database='datosComunales')

# Crear un cursor para ejecutar consultas
cursor = cnx.cursor()
stay="y"

while (stay=="y"):
	op=input("opciones:\n1. Listado de region con X o mas habitantes \n 2.Listado de comunas y su densidad poblacional de una region especifica\n3. Promedio de personas por vivienda de comunas de una region dada \n4. Cantidad de jardines infantiles por comuna de una region\n5. Listado de establecimientos municipales\n6.\n7. Establecimientos pace\n8.\n9.\n10.\n11.\n12.\n13.\n14.\n")

	
	if (op=="1") :
		rer=str(input("Listado de regiones con x o mas habitantes, ingrese x con numero entero:"))
		consulta="select nombre, poblacion from comuna Where poblacion>"+rer
		cursor.execute(consulta)
		resultados=cursor.fetchall()
		#print("--------------------------------")
		for resultado in resultados:
			comuna= resultado[1]
			print("| {:<25} |".format(comuna))
		#print("--------------------------------")

	if (op=="2") :
		rer=str(input("De que region desa el listado de densidad de poblacion(codigo numerico):"))
		consulta="select r.nombre, c.nombre, c.poblacion, c.superficie, c.poblacion/c.superficie as densidad_poblacional from region r JOIN comuna c ON r.idRegion = c.idRegion WHERE r.idRegion ="+rer+"  order by densidad_poblacional DESC;"
		cursor.execute(consulta)
		resultados=cursor.fetchall()
		#print("--------------------------------")
		for resultado in resultados:
			comuna= resultado[1]
			densidad= resultado[-1]
			#print("|",comuna,"           |",densidad,"|")
			print("| {:<25} | {:<10} |".format(comuna, densidad))
		#print("--------------------------------")

	if (op=="3") :
		rer=str(input("De que region desea el listado de habitantes promedio por vivienda(codigo numerico):"))
		consulta="select r.idRegion, r.nombre,  c.nombre, c.poblacion, c.viviendas, c.poblacion/c.viviendas as promedio_personas_por_vivienda from region r JOIN comuna c ON r.idRegion = c.idRegion WHERE r.idRegion ="+rer+"  order by densidad_poblacional DESC;"
		cursor.execute(consulta)
		resultados=cursor.fetchall()
		#print("--------------------------------")
		for resultado in resultados:
			comuna= resultado[1]
			habitantes_promedio_por_vivienda= resultado[-1]
			#print("|",comuna,"           |",densidad,"|")
			print("| {:<25} | {:<10} |".format(comuna, habitantes_promedio_por_vivienda))

	if (op=="4") :
		rer=str(input("De que region quiere la cantidad de jardines infantiles por comuna (codigo numerico):"))
		consulta=" select c.nombre, count(ed.idEstablecimiento) from establecimientoEducacion ed JOIN comuna c ON ed.idComuna = c.idComuna JOIN region r ON c.idRegion = r.idRegion WHERE ed.nombre LIKE '%Jardín%' AND r.idRegion ="+rer +"group by c.nombre;"
		cursor.execute(consulta)
		resultados=cursor.fetchall()
		#print("--------------------------------")
		for resultado in resultados:
			comuna= resultado[1]
			cant_jardines= resultado[-1]
			#print("|",comuna,"           |",densidad,"|")
			print("| {:<25} | {:<10} |".format(comuna, cant_jardines))
	
	if (op=="5") :
		rer=str(input("De que region quiere obtener el listado de establecimientos municipales (codigo numerico):"))
		consulta="select r.idRegion, c.idComuna, c.nombre, ed.nombre from establecimientoEducacion ed JOIN comuna c ON ed.idComuna = c.idComuna JOIN region r ON c.idregion = r.idregion where ed.nombre like '%municipal%' and idRegion="+rer+";"
		cursor.execute(consulta)
		resultados=cursor.fetchall()
		#print("--------------------------------")
		for resultado in resultados:
			comuna= resultado[-2]
			establecimiento= resultado[-1]
			#print("|",comuna,"           |",densidad,"|")
			print("| {:<25} | {:<10} |".format(comuna, establecimiento))

	if (op=="7") :
		rer=str(input("De que region quiere obtener la cantidad de establecimientos educacionales que participan en el programa pace (codigo numerico):"))
		consulta="select r.nombre, count(ed.idEstablecimiento) from establecimientoEducacion ed JOIN comuna c ON ed.idComuna = c.idComuna JOIN region r ON c.idRegion = r.idRegion where ed.PACE = 1 and idRegion ="+ rer +"group by r.nombre;"
		cursor.execute(consulta)
		resultados=cursor.fetchall()
		#print("--------------------------------")
		for resultado in resultados:
			comuna= resultado[1]
			cantidad= resultado[-1]
			#print("|",comuna,"           |",densidad,"|")
			print("| {:<25} | {:<10} |".format(comuna, cantidad))

	



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

