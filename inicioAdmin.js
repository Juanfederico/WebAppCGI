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
	document.getElementById("divAgregar").style.display = "inline";
}

function menuModificar(){}

function menuCancelar(){}