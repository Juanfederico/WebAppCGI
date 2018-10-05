/*$(document).ready(function(){
	alert("cargo el script");
});*/

function menuAgregar(){
	//Desde un JSON Array se cargan los horarios de apertura y clausura en los select correspondientes
	var jqxhr = $.getJSON( '/webappcgi/horarios.json', function(horarios) {
	})
	.done(function(horarios) {
		var options = "<option value='' selected disabled>Seleccionar</option>";
		$.each(horarios,function(key,value){
			options += '<option value='+value+'>'+value+'</option>';
		});
		$('#horario_apertura').html(options);
		$('#horario_cierre').html(options);
	})
	.fail(function(textStatus, error) {
		console.error('getJSON failed, status: ' + textStatus + ', error: '+error);
	})
	.always(function() {
	});

	//Se agregan los días de mantenimiento
	var dias = "<option value='' selected disabled>Seleccionar</option>";
	for(var i=1 ; i<=31 ; i++){
		dias += '<option value='+i+'>'+i+'</option>';
	}
	$('#dia_mantenimiento').html(dias);

	//Finalmente se visualiza el contenido en pantalla
	document.getElementById("divModificar").style.display = "none";
	document.getElementById("divAgregar").style.display = "inline";
}

function menuModificar(){

	//Finalmente se visualiza el contenido en pantalla
	document.getElementById("divAgregar").style.display = "none";
	document.getElementById("divModificar").style.display = "inline";
}


function detalleFilial(){
	var arrayData = $("#filial").val().split('/');
	var idfilial = arrayData[0];
	var localidad = arrayData[1];
	var horario_apertura = arrayData[2].substr(0, 5);
	var horario_cierre = arrayData[3].substr(0, 5);
	var dia_mantenimiento = arrayData[4];

	$("#mlocalidad").val(localidad);

	var jqxhr = $.getJSON( '/webappcgi/horarios.json', function(horarios) {
	})
	.done(function(horarios) {
		var options = "";
		$.each(horarios,function(key,value){
			if(String(horario_apertura)==String(value)) options += '<option value='+value+' selected>'+value+'</option>';
			else options += '<option value='+value+'>'+value+'</option>';
		});
		$('#mhorario_apertura').html(options);
		$.each(horarios,function(key,value){
			if(String(horario_cierre)==String(value)) options += '<option value='+value+' selected>'+value+'</option>';
			else options += '<option value='+value+'>'+value+'</option>';
		});
		$('#mhorario_cierre').html(options);
	})
	.fail(function(textStatus, error) {
		console.error('getJSON failed, status: ' + textStatus + ', error: '+error);
	})
	.always(function() {
	});

	//Se agregan los días de mantenimiento
	var dias = "";
	for(var i=1 ; i<=31 ; i++){
		if(dia_mantenimiento==i) dias += '<option value='+i+' selected>'+i+'</option>';
		else dias += '<option value='+i+'>'+i+'</option>';
	}
	$('#mdia_mantenimiento').html(dias);

	//$("#mhorario_apertura").val(""+String(horario_apertura)).change();
	document.getElementById("mhorario_apertura").selectedIndex = "2";
	//$("#mhorario_apertura[value='"+horario_apertura+"']").attr('selected',true);


}


function menuCancelar(){}