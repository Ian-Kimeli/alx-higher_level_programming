$(document).ready(function() {
    function translateHello() {
        const langCode = $('#language_code').val();
        const apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/';

        $.get(apiUrl + langCode, function(data) {
            $('#hello').text(data);
        }).fail(function() {
            $('#hello').text("Translation not found");
        });
    }

    // Button Click
    $('#btn_translate').click(translateHello); 

    // ENTER Keypress
    $('#language_code').keypress(function(event) {
        if (event.key === "Enter" || event.keyCode === 13) { 
            translateHello(); 
        }
    });
});

