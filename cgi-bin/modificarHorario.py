#!C:\Python27\python.exe
# Import modules for CGI handling 
import pyodbc
import cgi, cgitb
import os, sys, json
# Create instance of FieldStorage 
form = cgi.FieldStorage()   #Levanto datos del formulario

if form.getvalue('subject'):
   subject = form.getvalue('subject')
else:
   subject = "Not set"

arrayPrueba = []

conn = pyodbc.connect(DSN="bdsistemaclub")
cursor = conn.cursor()
sql = "SELECT * from admin where user='"+form.getvalue("user")+"' AND pass='"+form.getvalue("pass")+"'"
cursor.execute(sql)
rows = cursor.fetchall()
for row in rows:
	arrayPrueba.append(row.user)

if not rows: #Login incorrecto
	print "Content-type:text/html\r\n\r\n"
	print "<html>"
	print "<head>"
	print "<title>Login admin - Club Los Amigos</title>"
	print "<script src='https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js'></script>"
	print "</head>"
	print "<body>"

	print "<meta http-equiv='refresh' content='0; url=/webappcgi/index.html?login=false' />"
	print "</body>"

else: #Login correcto
	print "Content-type:text/html\r\n\r\n"
	print "<html>"
	print "<head>"
	print "<title>Panel admin - Club Los Amigos</title>"
	print "</head>"
	print "<body>"

	print "<strong>Logueado correctamente como: </strong>" + arrayPrueba[0]
	print "<br><br><br>"

	print "<strong> Seleccione la accion a realizar: </strong><br>"
	print "<form action='/cgi-bin/agregarFilial.py' method='post'>"
	print "<input type='submit' name='agregar' value='Agregar filial'>"
	print "<form action='/cgi-bin/cancelarTurno.py' method='post'>"
	print "<input type='submit' name='cancelar' value='Cancelar turno'>"
	print "<form action='/cgi-bin/modificarHorario.py' method='post'>"
	print "<input type='submit' name='modificar' value='Modificar dia u horario de filial'>"

	#print(os.environ['HTTP_REFERER']) VARIABLE DE ENTORNO - URL QUE INVOCO AL CGI
	#print(os.environ['SERVER_PORT']) VARIABLE DE ENTORNO - PUERTO TCP DONDE SE ACCEDE AL CGI
	#print(os.environ['REQUEST_METHOD']) VARIABLE DE ENTORNO - METODO POR DONDE SE PASA LA DATA

	#print form.getvalue("user") #LEVANTA LA DATA DEL TEXT CONTENT
	#print form["user"].value #OTRA FORMA
	#print "<br><br><br>"
	#print "<h2> Entered Text Content is "+form.getvalue("user")+"</h2>"
	#print "Contrasenia: "+form.getvalue("pass")
	print "</body>"