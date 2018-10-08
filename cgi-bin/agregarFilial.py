#!C:\Python27\python.exe
# Import modules for CGI handling 
import pyodbc
import cgi, cgitb
import os, sys, json
# Create instance of FieldStorage 
form = cgi.FieldStorage()   #Levanto datos del formulario

arrayPrueba = []

conn = pyodbc.connect(DSN="bdsistemaclub")
cursor = conn.cursor()

sql = "INSERT INTO filial (localidad, horario_apertura, horario_cierre, diames_mantenimiento) VALUES ('"+form.getvalue("localidad")+"', '"+form.getvalue("horario_apertura")+"', '"+form.getvalue("horario_cierre")+"', "+form.getvalue("dia_mantenimiento")+")"
cantidad = cursor.execute(sql)
conn.commit()

sql = "SELECT MAX(idFilial) FROM filial" #Se va a buscar el ultimo id insertado para agregarle las canchas
cantidad = cursor.execute(sql)
nuevoId = cursor.fetchall()


idFilial = nuevoId[0][0] # idFilial es igual a ultimo id insertado

# Se agregan canchas de prueba. Esto no es a modo de prueba, para poder alquilar canchas sobre sobre la sede
sql = "INSERT INTO cancha (idfilial, num_cancha, deporte, categoria) VALUES (" + str(idFilial) + ", '1', 'Futbol', 'Sintetico')"
cantidad = cursor.execute(sql)
conn.commit()

sql = "INSERT INTO cancha (idfilial, num_cancha, deporte, categoria) VALUES (" + str(idFilial) + ", '2', 'Tenis', 'Cemento')"
cantidad = cursor.execute(sql)
conn.commit()

sql = "INSERT INTO cancha (idfilial, num_cancha, deporte, categoria) VALUES (" + str(idFilial) + ", '3', 'Basquet', 'Madera')"
cantidad = cursor.execute(sql)
conn.commit()


print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Agregar filial</title>"
print "<link href='../WebAppCGI/css/style.css' rel='stylesheet'>"
print "<link href='../WebAppCGI/css/bootstrap.min.css' rel='stylesheet'>"
print "</head>"
print "<body>"
if cantidad is not None:
	print "<div class='row'>"  
	print "<div class='col-lg-10'>"
	print "<div class='card-body'>"
	print "<h4 class='card-title'>Filial agregada correctamente </h4>"
	print "<h5 class='card-title'>Localidad: " + form.getvalue("localidad") + "</h5>"
	print "<h5 class='card-title'>Horario de apertura: " + form.getvalue("horario_apertura") + "</h5>"
	print "<h5 class='card-title'>Horario de cierre: " + form.getvalue("horario_cierre") + "</h5>"
	print "<h5 class='card-title'>Dia de mantenimiento: " + form.getvalue("dia_mantenimiento") + "</h5>"
	print "<div class='col-lg-3'>"
	print "<form action='/cgi-bin/inicioAdmin.py' method='POST'>"
	print "<input type='hidden' name='user' value='"+form.getvalue("user")+"'>"
	print "<input class='btn btn-info btn-block waves-effect waves-light' type='submit' value='Volver'>"
	print "</div>" # class='col-lg-3'
	print "</div>" # class='card-body'
	print "</div>" # class='col-lg-10'
	print "</div>" # class='row'
else:
	print "Error al insertar filial"



print "</body>"