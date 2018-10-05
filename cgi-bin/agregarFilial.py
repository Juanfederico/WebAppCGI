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
#sql = "SELECT * from admin where user='"+form.getvalue("user")+"' AND pass='"+form.getvalue("pass")+"'"
sql = "INSERT INTO filial (localidad, horario_apertura, horario_cierre, diames_mantenimiento) VALUES ('"+form.getvalue("localidad")+"', '"+form.getvalue("horario_apertura")+"', '"+form.getvalue("horario_cierre")+"', "+form.getvalue("dia_mantenimiento")+")"
cantidad = cursor.execute(sql)
conn.commit()

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Buscar socio</title>"
print "</head>"
print "<body>"
if cantidad is not None:
	print "<b>Filial insertada correctamente:</b><br>"
	print form.getvalue("localidad") + "<br>"
	print form.getvalue("horario_apertura") + "<br>"
	print form.getvalue("horario_cierre") + "<br>"
	print form.getvalue("dia_mantenimiento") + "<br>"
else:
	print "Error al insertar filial"

print "<a href='javascript:history.back()'>"
print "<input type='button' value='Volver'>"
print "</a>"

print "</body>"