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

turnos = form.getlist("turnoACancelar[]")

for idTurno in turnos:
	sql = "UPDATE turno SET estado='cancelada' WHERE idturno=" + idTurno
	cantidad = cursor.execute(sql)
	conn.commit()

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Cancelar turno</title>"
print "<link href='../WebAppCGI/css/style.css' rel='stylesheet'>"
print "<link href='../WebAppCGI/css/bootstrap.min.css' rel='stylesheet'>"
print "</head>"
print "<body>"


if cantidad is not None:
	print "<div class='row'>"  
	print "<div class='col-lg-10'>"
	print "<div class='card-body'>"
	if (len(turnos) > 1):
		print "<h4 class='card-title'>Turnos cancelados correctamente </h4>"
	else:
		print "<h4 class='card-title'>Turno cancelado correctamente </h4>"
	print "<div class='col-lg-3'>"
	print "<form action='/cgi-bin/inicioAdmin.py' method='POST'>"
	print "<input type='hidden' name='user' value='" +form.getvalue("user")+ "'>"
	print "<input class='btn btn-info btn-block waves-effect waves-light' type='submit' value='Volver'>"
	print "</div>" # class='col-lg-3'
	print "</div>" # class='card-body'
	print "</div>" # class='col-lg-10'
	print "</div>" # class='row'
else:
	print "Error al cancelar el turnos"


print "</body>"