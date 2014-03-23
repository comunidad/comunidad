$(document).on('ready', main);

function main () {
	$('#articulo').on('click', 'a', cargar_contenido_articulo);
}

function cargar_contenido_articulo(data) {
	var id = $(data.currentTarget).data('id');

	$.get('cargar-contenido-articulo/' + id, cargar_articulo)
}

function cargar_articulo(data){
	var contenido = $('#contenido-articulo');
	
	contenido_articulo.html('');

	$('<a class="regresar">').html('Regresar').appendTo(contenido_articulo);

	$('<h2>').html(data.titulo).appendTo(contenido-articulo);

	//$('<iframe src="http://www.youtube.com/embed/' + data.url + '" allowfullscreen>').appendTo(contenido);

	$('<p>').html(data.contenido_articulo).appendTo(contenido_articulo);

	$('#articulos').css('left', '-110%');
	contenido.css('left', '0');

	contenido.on('click', 'a', function(){
		contenido.css('left', '-110%');
		$('#articulos').css('left', '0');
	});
}