/* Most of the code from Code institute */
let countrySelected = $('#id_default_country').val();
if (!countrySelected) {
    $('#id_default_country').css('color', '#a3c284');
}
$('#id_default_country').change(function () {
    countrySelected = $(this).val();
    if (!countrySelected) {
        $(this).css('color', '#a3c284');
    } else {
        $(this).css('color', '#000');
    }
});