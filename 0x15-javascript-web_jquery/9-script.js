<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script>
$(document).ready(function() {
    $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
        $('#hello').text(data.hello);
    });
});
</script>

