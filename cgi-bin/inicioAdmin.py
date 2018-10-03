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
	print "<script src='https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js'></script>"
	print "<script type='application/javascript' src='/webappcgi/inicioAdmin.js'></script>"

	print "</head>"
	print "<body>"

	print "<strong>Logueado correctamente como: </strong>" + arrayPrueba[0]
	print "<br><br><br>"

	print "<strong> Seleccione la accion a realizar: </strong><br>"
	print "<div id=divOpciones>"
	print "<button id='agregarFilial' onclick='menuAgregar()'>Agregar filial</button>"
	print "<button id='modificarHorario' onclick='menuModificar()'>Modificar dia u horarios de filial</button>"
	print "<button id='cancelarTurno' onclick='menuCancelar()'>Cancelar turno</button>"
	print "</div>"

	print "<form method='post'>"
	print "<input type='hidden' name='user' value='" +form.getvalue("user")+ "'>"
	#print "<input type='submit' value='Modificar dia u horarios de filial' formaction='/cgi-bin/modificarHorario.py'>"
	#print "<input type='submit' value='Cancelar turno' formaction='/cgi-bin/cancelarTurno.py'>"


	print "<br><br><br>"

	print "<div id='divAgregar' style='display: none;'>"       #style='display: none;'
	print "<strong>Localidad: </strong>"
	print "<input type='text' name='localidad'><br>"
	print "<strong>Horario de apertura: </strong>"
	print "<select id='horario_apertura'>"
	print "</select><br>"
	print "<strong>Horario de cierre: </strong>"
	print "<select id='horario_cierre'>"
	print "</select><br>"
	print "<strong>Dia de mantenimiento: </strong>"
	print "<select id='dia_mantenimiento'>"
	print "</select><br>"
	print "<input type='submit' value='Agregar filial' formaction='/cgi-bin/agregarFilial.py'>"
	print "</div>"

	print "<div id='modificar'>"
	print "</div>"

	#print "<div id='cancelar'>"
	#print "</div>"
    #print "<input type='submit' value='Modificar dia u horarios de filial' formaction='/cgi-bin/modificarHorario.py'>"
    #print "<button formaction='cancelarTurno.py'>Cancelar turno</button>"
    #print "<input type='submit' value='asd'>"

    #print "</form>"
	print "</body>"