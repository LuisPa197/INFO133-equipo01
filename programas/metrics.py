import mysql.connector

# Conexión a la base de datos
cnx = mysql.connector.connect(user='root', password='info10000',
                              host='localhost',
                              database='datosComunales')

# Crear un cursor para ejecutar consultas
cursor = cnx.cursor()
stay="y"

while (stay=="y"):
	op=input("opciones:\n1. Listado de region con X o mas habitantes\n2. Listado de comunas y su densidad poblacional de una region especifica\n3. Promedio de personas por vivienda de comunas de una region dada \n4. Cantidad de jardines infantiles por comuna de una region\n5. Listado de establecimientos municipales\n6. lista de centros de salud y dirección por comuna\n7. Establecimientos pace\n8. Densidad de centros educacionales por comuna\n9. Densidad de centros de salud por comuna\n10. Top x comunas comunas con el mayor indice de DMCS\n11. Maximo y minimo de indice de DMCS de una region\n12. Top x conexiones per capita de una region\n13. Indice de vulnerabilidad por comuna\n14. Número de comunas por región\n")

	
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

	if (op=="6") :
		rer=str(input("De que comuna quiere obtener el listado de centro de salud (nombre comuna):"))
		consulta="select s.idCentro, s.nombre, s.direccion from centroSalud s JOIN comuna c ON s.idComuna = c.idComuna where c.nombre = '"+rer+"';"
		cursor.execute(consulta)
		resultados=cursor.fetchall()
		#print("--------------------------------")
		for resultado in resultados:
			idC= resultado[0]
			establecimiento= resultado[-2]
			direccion= resultado[-1]
			#print("|",comuna,"           |",densidad,"|")
			print("| {:<10} | {:<60} | {:<50}".format(idC, establecimiento, direccion))

	if (op=="7") :
		rer=str(input("De que region quiere obtener la cantidad de establecimientos educacionales que participan en el programa pace (codigo numerico):"))
		consulta="select r.nombre, count(ed.idEstablecimiento) from establecimientoEducacion ed JOIN comuna c ON ed.idComuna = c.idComuna JOIN region r ON c.idRegion = r.idRegion where ed.PACE = 1 and idRegion ='"+ rer +"'group by r.nombre;"
		cursor.execute(consulta)
		resultados=cursor.fetchall()
		#print("--------------------------------")
		for resultado in resultados:
			comuna= resultado[1]
			cantidad= resultado[-1]
			#print("|",comuna,"           |",densidad,"|")
			print("| {:<25} | {:<10} |".format(comuna, cantidad))

	if (op=="8") :
		consulta="select c.nombre, count(ed.idEstablecimiento)/c.superficie as establecimientos_de_educacion_por_km2 from establecimientoEducacion ed JOIN comuna c ON ed.idComuna = c.idComuna group by c.nombre;"
		cursor.execute(consulta)
		resultados=cursor.fetchall()
		#print("--------------------------------")
		for resultado in resultados:
			comuna= resultado[0]
			cantidad= resultado[-1]
			#print("|",comuna,"           |",densidad,"|")
			print("| {:<25} | {:<10} |".format(comuna, cantidad))	

	if (op=="9") :
		consulta="select c.nombre, count(sa.idCentro)/c.superficie as centros_de_salud_por_km2 from centroSalud sa JOIN comuna c ON sa.idComuna = c.idComuna group by c.nombre;"
		cursor.execute(consulta)
		resultados=cursor.fetchall()
		#print("--------------------------------")
		for resultado in resultados:
			comuna= resultado[0]
			cantidad= resultado[-1]
			#print("|",comuna,"           |",densidad,"|")
			print("| {:<25} | {:<10} |".format(comuna, cantidad))	

	if (op=="10") :
		rer=str(input("Cuántas comunas desea desplegar para el top de tasa DMCS (numérico):"))
		consulta="select c.nombre, s.tasaDenunciasDMCS from seguridad s JOIN comuna c ON s.idComuna = c.idComuna order by s.tasaDenunciasDMCS DESC LIMIT "+rer+";"
		cursor.execute(consulta)
		resultados=cursor.fetchall()
		#print("--------------------------------")
		for resultado in resultados:
			comuna= resultado[0]
			cantidad= resultado[-1]
			#print("|",comuna,"           |",densidad,"|")
			print("| {:<25} | {:<10} |".format(comuna, cantidad))

	if (op=="11") :
		rer=str(input("De que region quiere obtener las comunas con maximo y minimo de DMCs (codigo numerico):"))
		consulta="select c.nombre, s.tasaDenunciasDMCS from seguridad s JOIN comuna c ON s.idComuna = c.idComuna JOIN region r ON c.idRegion = r.idRegion WHERE c.idRegion = "+rer+" order by s.tasaDenunciasDMCS DESC LIMIT 1;"
		cursor.execute(consulta)
		resultados=cursor.fetchall()
		print("Maximo:")
		for resultado in resultados:
			comuna= resultado[0]
			cantidad= resultado[-1]
			#print("|",comuna,"           |",densidad,"|")
			print("| {:<25} | {:<10} |".format(comuna, cantidad))
		consulta="select c.nombre, s.tasaDenunciasDMCS from seguridad s JOIN comuna c ON s.idComuna = c.idComuna JOIN region r ON c.idRegion = r.idRegion WHERE c.idRegion ="+rer+" order by s.tasaDenunciasDMCS ASC LIMIT 1;"
		cursor.execute(consulta)
		resultados=cursor.fetchall()
		print("Minimo:")
		for resultado in resultados:
			comuna= resultado[0]
			cantidad= resultado[-1]
			#print("|",comuna,"           |",densidad,"|")
			print("| {:<25} | {:<10} |".format(comuna, cantidad))

	if (op=="12") :
		rer=str(input("De que region quiere obtener la cantidad de conexiones per capita (codigo numerico):"))
		rel=str(input("Cuantas quiere que se desplieguen (numerico):"))
		consulta="SELECT c.nombre, c.poblacion AS conexiones_per_capita FROM conectividad co JOIN comuna c ON co.idComuna = c.idComuna JOIN region r ON c.idRegion = r.idRegion WHERE c.idRegion = "+rer+" LIMIT "+rel+";"
		cursor.execute(consulta)
		resultados=cursor.fetchall()
		#print("--------------------------------")
		for resultado in resultados:
			comuna= resultado[0]
			cantidad= resultado[-1]
			#print("|",comuna,"           |",densidad,"|")
			print("| {:<25} | {:<10} |".format(comuna, cantidad))		

	if (op=="13") :
		rer=str(input("De que region quiere los indices de vulnerabilidad por couma (codigo numerico):"))
		consulta="select c.nombre, s.indiceVulnerabilidad from seguridad s JOIN comuna c ON s.idComuna = c.idComuna JOIN region r ON c.idRegion = r.idRegion where c.idRegion = "+rer+" order by s.indiceVulnerabilidad;"
		cursor.execute(consulta)
		resultados=cursor.fetchall()
		#print("--------------------------------")
		for resultado in resultados:
			comuna= resultado[0]
			cantidad= resultado[-1]
			#print("|",comuna,"           |",densidad,"|")
			print("| {:<25} | {:<10} |".format(comuna, cantidad))

	if(op=="14") :
		consulta="select r.nombre, count(c.idComuna) from comuna c JOIN region r ON c.idRegion = r.idRegion group by r.nombre;"
		cursor.execute(consulta)
		resultados=cursor.fetchall()	
		for resultado in resultados:
			region = resultado[0]
			cantidad = resultado[-1]
			print("| {:<42} | {:<10} |".format(region, cantidad))


	stay=input("Desea realizar otra consulta y/n?:")
cursor.close()
cnx.close()

