$(document).ready(function() {
    $('#btn_translate').click(function() {
        const langCode = $('#language_code').val(); 
        const apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/';

        $.get(apiUrl + langCode, function(data) { 
            $('#hello').text(data); 
        }).fail(function() {
            // Error handling in case the API request fails
            $('#hello').text("Translation not found");
        });
    });
});

