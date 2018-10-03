#!C:\Python27\python.exe
# Import modules for CGI handling 
import pyodbc
import cgi, cgitb
import os, sys, json
# Create instance of FieldStorage 
form = cgi.FieldStorage()   #Levanto datos del formulario

conn = pyodbc.connect(DSN="bdsistemaclub")
cursor = conn.cursor()
sql = "SELECT * from socio WHERE num_afiliado="+form.getvalue("numafiliado")
cursor.execute(sql)
rows = cursor.fetchall()

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Datos socio numero " +form.getvalue("numafiliado")+ "</title>"

for row in rows:
	print "Nombre: " +row.nombre+ "<br>"
	print "Apellido: " +row.apellido+ "<br>"
	print "Correo electronico: " +row.email+ "<br>"

print "</head>"
print "<body>"

for elem in arrayPrueba:
	print elem

print "</body>"