// These are inspired from Code Institute lessons

// Disable +/- buttons outside 1-40 range
function handleEnableDisableRental(id) {
    let currentValue = parseInt($(`#id_qty_${id}`).val());
    let minusDisabled = currentValue < 2;
    let plusDisabled = currentValue > 39;
    $(`#decrement-qty_${id}`).prop('disabled', minusDisabled);
    $(`#increment-qty_${id}`).prop('disabled', plusDisabled);
}

// Ensure proper enabling/disabling of all inputs on page load
let allQtyInputsRental = $('.qty_input_rental');
for (let i = 0; i < allQtyInputsRental.length; i++) {
    let id = $(allQtyInputsRental[i]).data('id');
    handleEnableDisableRental(id);
}

// Check enable/disable every time the input is changed
$('.qty_input_rental').change(function () {
    let id = $(this).data('id');
    handleEnableDisableRental(id);
});

// Increment quantity
$('.increment-qty_rental').click(function (e) {
    e.preventDefault();
    let closestInput = $(this).closest('.input-group').find('.qty_input_rental')[0];
    let currentValue = parseInt($(closestInput).val());
    $(closestInput).val(currentValue + 1);
    let id = $(this).data('id');
    handleEnableDisableRental(id);
});

// Decrement quantity
$('.decrement-qty_rental').click(function (e) {
    e.preventDefault();
    let closestInput = $(this).closest('.input-group').find('.qty_input_rental')[0];
    let currentValue = parseInt($(closestInput).val());
    $(closestInput).val(currentValue - 1);
    let id = $(this).data('id');
    handleEnableDisableRental(id);
});