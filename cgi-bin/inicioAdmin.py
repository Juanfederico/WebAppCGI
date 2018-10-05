#!C:\Python27\python.exe
# Import modules for CGI handling 
import pyodbc
import cgi, cgitb
import os, sys, json
# Create instance of FieldStorage 
form = cgi.FieldStorage()   #Levanto datos del formulario

#Nombre de usuario para autenticacion
arrayUser = []

#Estableciendo la conexion por ODBC
conn = pyodbc.connect(DSN="bdsistemaclub")
cursor = conn.cursor()
#Primera query (autenticacion del usuario)
sql = "SELECT * from admin where user='"+form.getvalue("user")+"' AND pass='"+form.getvalue("pass")+"'"
cursor.execute(sql)
rows = cursor.fetchall()
for row in rows:
	arrayUser.append(row.user)
#Segunda query (informacion de todas las filiales)
sql = "SELECT * from filial"
cursor.execute(sql)
rows = cursor.fetchall() #Se utiliza a lo largo del programa para cargar los select

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

	print "<strong>Logueado correctamente como: </strong>" + arrayUser[0]
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
	print "<strong>Seleccione la filial que desea modifiar</strong><br>"
	print "<select id='filial'>"
	print "<option selected disabled>Seleccionar</option>"
	for row in rows:
		print "<option value='"+str(row.idfilial)+"'>"+row.localidad+"</option>"
	print "</select><br>"
	print "</div>"

	#print "<div id='cancelar'>"
	#print "</div>"
    #print "<input type='submit' value='Modificar dia u horarios de filial' formaction='/cgi-bin/modificarHorario.py'>"
    #print "<button formaction='cancelarTurno.py'>Cancelar turno</button>"
    #print "<input type='submit' value='asd'>"

    #print "</form>"
	print "</body>"