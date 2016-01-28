$(document).ready(function() {
	$.get('http://192.168.24.10:10001/', function(data) {
		$('#video').html(`<video id="video" width="640" controls>
    		<source src="` + data.directory + `" type="video/mp4">
		</video>`);
	});
});