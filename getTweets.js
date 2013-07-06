$(function() {
  // Twitter feed
	$.ajax({
		url: 'YOUR_URL',
		type: 'POST',
		dataType: 'json',
		success: function(data, textStatus, xhr) {
			var html = '';
			for (var i = 0; i < data.length; i++) {
        			// Adjust the markup to suit your needs
				html = html +'<li class="latest-tweet"><p>' + data[i] + '</p></li>';
			}
		$('#mytweets').append(html);
		}
	});
});
