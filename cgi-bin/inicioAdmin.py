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

#Tercera query (informacion de todas los turnos)
sql = "SELECT * from turno"
cursor.execute(sql)
turnos = cursor.fetchall() #Se utiliza a lo largo del programa para cargar los select

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
	print "<meta charset='utf-8'>"
	print "<link href='../WebAppCGI/css/style.css' rel='stylesheet'>"
	print "<link href='../WebAppCGI/css/bootstrap.min.css' rel='stylesheet'>"
	print "<script src='https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js'></script>"
	print "<script type='application/javascript' src='/webappcgi/inicioAdmin.js'></script>"

	print "</head>"
	
	print "<div class='row'>"  
	print "<div class='col-lg-10'>"
	print "<div class='card-body'>"
	print "<h3 class='card-title'>Bienvenido: "+ arrayUser[0]+"</h3>"
	print "<h4 class='card-title'> Seleccione la accion a realizar: </h4>"
	print "<div id=divOpciones>"
	print "<div class='row'>"
	print "<div class='col-lg-3'>"
	print "<button class='btn btn-info btn-block waves-effect waves-light' onclick='menuAgregar()'>Agregar filial</button>"
	print "<button class='btn btn-info btn-block waves-effect waves-light' onclick='menuModificar()'>Modificar dia u horarios de filial</button>"
	print "<button class='btn btn-info btn-block waves-effect waves-light' onclick='menuCancel()'>Cancelar turno</button>"
	print "</div>" # class='col-lg-3'
	print "</div>" # class='row'
	print "</div>" # id=divOpciones
	print "</div>" # class='card-body'
	print "</div>" # class='col-lg-10'
	print "</div>" # class='row'
	

	print "<form method='post'>"
	print "<input type='hidden' name='user' value='" +form.getvalue("user")+ "'>"
	#print "<input type='submit' value='Modificar dia u horarios de filial' formaction='/cgi-bin/modificarHorario.py'>"
	#print "<input type='submit' value='Cancelar turno' formaction='/cgi-bin/cancelarTurno.py'>"



	print "<div id='divAgregar' style='display: none;'>" #style='display: none;'
	print "<div class='row'>"  
	print "<div class='col-lg-10'>"
	print "<div class='card-body'>"
	print "<h4 class='card-title'> Agregar filial: </h4>"
	print "<div class='form-group'>"       
	print "<strong>Localidad: </strong>"
	print "<input type='text' name='localidad'>"
	print "</div>" # class='form-group'
	print "<div class='form-group'>"    
	print "<strong>Horario de apertura: </strong>"
	print "<select id='horario_apertura' name='horario_apertura'>"
	print "</select>"
	print "</div>" # class='form-group'
	print "<div class='form-group'>"  
	print "<strong>Horario de cierre: </strong>"
	print "<select id='horario_cierre' name='horario_cierre'>"
	print "</select>"
	print "</div>" # class='form-group'
	print "<div class='form-group'>"  
	print "<strong>Dia de mantenimiento: </strong>"
	print "<select id='dia_mantenimiento' name='dia_mantenimiento'>"
	print "</select>"
	print "</div>" # class='form-group'
	print "<div class='col-lg-3'>"
	print "<input class='btn btn-info btn-block waves-effect waves-light' type='submit' value='Agregar filial' formaction='/cgi-bin/agregarFilial.py'>"
	print "</div>" # class='col-lg-3'
	print "</div>" # id=divAgregar
	print "</div>" # class='card-body'
	print "</div>" # class='col-lg-10'
	print "</div>" # class='row'



	print "<div id='divModificar' style='display: none;'>"
	print "<div class='row'>"  
	print "<div class='col-lg-10'>"
	print "<div class='card-body'>"
	print "<h4 class='card-title'> Modificar filial: </h4>"
	print "<strong>Seleccione la filial que desea modifiar</strong><br>"
	print "<div class='form-group'>"
	print "<select id='filial'>"
	print "<option selected disabled>Seleccionar</option>"
	for row in rows:
		print "<option value='"+str(row.idfilial)+"/"+row.localidad+"/"+str(row.horario_apertura)+"/"+str(row.horario_cierre)+"/"+str(row.diames_mantenimiento)+"'>"+row.localidad+"</option>"
	print "</select>"
	print "</div>" # class='form-group'
	print "<div class='col-lg-3'>"  
	print "<button class='btn btn-info btn-block waves-effect waves-light' type='button' id='consultar' onclick='detalleFilial()'>Consultar</button>"
	print "</div>" # class='col-lg-3'
	print "</div>" # id=divModificar
	print "</div>" # class='card-body'
	print "</div>" # class='col-lg-10'
	print "</div>" # class='row'




	print "<div id='divCamposModificacion' style='display: none;'>"
	print "<div class='row'>"  
	print "<div class='col-lg-10'>"
	print "<div class='card-body'>"
	print "<input type='hidden' id='midfilial' name='midfilial'><br>"
	print "<div class='form-group'>"
	print "<strong>Localidad: </strong>"
	print "<input type='text' id='mlocalidad' name='mlocalidad'><br>"
	print "</div>" # class='form-group'
	print "<div class='form-group'>"
	print "<strong>Horario de apertura: </strong>"
	print "<select id='mhorario_apertura' name='mhorario_apertura'>"
	print "</select>"
	print "</div>" # class='form-group'
	print "<div class='form-group'>"
	print "<strong>Horario de cierre: </strong>"
	print "<select id='mhorario_cierre' name='mhorario_cierre'>"
	print "</select>"
	print "</div>" # class='form-group'
	print "<div class='form-group'>"
	print "<strong>Dia de mantenimiento: </strong>"
	print "<select id='mdia_mantenimiento' name='mdia_mantenimiento'>"
	print "</select>"
	print "</div>" # class='form-group'
	print "<div class='col-lg-3'>"  
	print "<input class='btn btn-info btn-block waves-effect waves-light' type='submit' value='Modificar Filial' formaction='/cgi-bin/modificarFilial.py'>"
	print "</div>" # class='col-lg-3'
	print "</div>" # id=divCamposModificacion
	print "</div>" # class='card-body'
	print "</div>" # class='col-lg-10'
	print "</div>" # class='row'


	print "<div id='divCancelarTurno' style='display: none;'>"
	print "<div class='row'>"  
	print "<div class='col-lg-6'>"
	print "<div class='card-body'>"
	print "<h4 class='card-title'> Cancelar turno: </h4>"
	print "<strong>Seleccione el turno que desea cancelar</strong><br>"
	print "<table class='table'>"
	print "<thead>"
	print "<tr>"
	print "<th>Filial</th>"
	print "<th>Cancha</th>"
	print "<th>Socio</th>"
	print "<th>Horario</th>"
	print "<th>Estado</th>"
	print "<th>Cancelar</th>"
	print "</tr>"
	print "</thead>"
	print "<tbody>"
	for row in turnos:
		print "<tr>"
		print "<td>"+str(row.idfilial)+"</td>"
		print "<td>"+str(row.idcancha)+"</td>"
		print "<td>"+str(row.idsocio)+"</td>"
		print "<td>"+str(row.fechahora)+"</td>"
		print "<td>"+str(row.estado)+"</td>"
		print "<td>"
		if (row.estado == "reservada"):
			print "<input type='checkbox' value='"+str(row.idturno)+"' id='turnoACancelar' name='turnoACancelar'>"
		print "</td>"
		#'+str(row.idfilial)+', '+str(row.idcancha)+', '+str(row.idsocio)+', '+str(row.fechahora)+', '+str(row.estado)+'  
		#print "<td><input class='btn btn-info btn-block waves-effect waves-light' type='submit' value='Cancelar Turno' formaction='/cgi-bin/cancelarTurno.py'></td>"
		print "</tr>"
		#print str(row.idturno)+"/"+
		#print str(row.idfilial)+"/"+str(row.idcancha)+"/"+str(row.idsocio)+"/"+str(row.fechahora)+"/"+row.estado
	print "</tbody>"
	print "</table>"
	print "<div class='col-lg-3'>"  
	print "<input class='btn btn-info btn-block waves-effect waves-light' type='submit' value='Cancelar Turnos' formaction='/cgi-bin/cancelarTurno.py'>"
	print "</div>" # class='col-lg-3'
	print "</div>" # id=divModificar
	print "</div>" # class='card-body'
	print "</div>" # class='col-lg-10'
	print "</div>" # class='row'

	print "</form>"

	print "<div id='cancelar'>"
	print "</div>"

	print "<script>"
	print "var btnCancelar = document.getElementById('btnCancelar');"
	print "btnCancelar.onclick = myfunction;"
	print "</script>"

	print "</body>"