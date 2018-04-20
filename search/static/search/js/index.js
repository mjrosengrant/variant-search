var api_url;
var gene_choices;

$(document).ready(function() {
	$('#btnSubmit').click(function() {
		query = $('#searchbox').val();
		$.ajax({
			type: 'GET',
			dataType: 'json',
			url: api_url + "?query=" + query,
			success: function (responseData, textStatus, jqXHR) {
				var output = ''
				$.each(responseData, function (i, variant) {
					output+= '<tr>'  + 
							 '<td>' + variant.gene + '</td>' +
							 '<td>' + variant.nucleotide_change + '</td>' +
							 '<td>' + variant.protein_change + '</td>' +
							 '<td>' + variant.alias + '</td>' +
							 '<td>' + variant.region + '</td>' +
							 '<td>' + variant.reported_classification + '</td>' +
							 '<td>' + variant.last_evaluated + '</td>' +
							 '<td>' + variant.last_updated + '</td>' +
							 '</tr>'
				});
				$("#variantTable > tbody tr").remove();
				$('#variantTable').find('tbody:last').append(output);

			},
			error: function () {
				console.log('GET failed');
			}
		});
	});
	$( "#searchbox" ).autocomplete({source: gene_choices});
});
