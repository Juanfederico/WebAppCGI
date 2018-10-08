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

idFilial = form.getvalue("midfilial")
localidad = form.getvalue("mlocalidad")
horario_apertura = form.getvalue("mhorario_apertura")
horario_cierre = form.getvalue("mhorario_cierre")
diames_mantenimiento= form.getvalue("mdia_mantenimiento")


sql = "UPDATE `filial` SET `localidad` = '" + localidad + "', `horario_apertura` = '" + horario_apertura + "', `horario_cierre` = '" + horario_cierre + "', `diames_mantenimiento` = '" + diames_mantenimiento + "' WHERE `filial`.`idFilial` = '" + idFilial + "';"
cantidad = cursor.execute(sql)
conn.commit()

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Modificar filial</title>"
print "<link href='../WebAppCGI/css/style.css' rel='stylesheet'>"
print "<link href='../WebAppCGI/css/bootstrap.min.css' rel='stylesheet'>"
print "</head>"
print "<body>"

if cantidad is not None:
	print "<div class='row'>"  
	print "<div class='col-lg-10'>"
	print "<div class='card-body'>"
	print "<h4 class='card-title'>Filial modificada correctamente </h4>"
	print "<h5 class='card-title'>Localidad: " + localidad + "</h5>"
	print "<h5 class='card-title'>Horario de apertura: " + horario_apertura + "</h5>"
	print "<h5 class='card-title'>Horario de cierre: " + horario_cierre + "</h5>"
	print "<h5 class='card-title'>Dia de mantenimiento: " + diames_mantenimiento + "</h5>"
	print "<div class='col-lg-3'>"
	print "<form action='/cgi-bin/inicioAdmin.py' method='POST'>"
	print "<input type='hidden' name='user' value='"+form.getvalue("user")+"'>"
	print "<input class='btn btn-info btn-block waves-effect waves-light' type='submit' value='Volver'>"
	print "</div>" # class='col-lg-3'
	print "</div>" # class='card-body'
	print "</div>" # class='col-lg-10'
	print "</div>" # class='row'
else:
	print "Error al modificar filial"

print "</body>"