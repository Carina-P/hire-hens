// MONTHS //
// Disable +/- buttons outside 1-40 range
function handleEnableDisableMonths() {
    let currentValue = parseInt($(`#id_months`).val());
    let minusDisabled = currentValue < 2;
    let plusDisabled = currentValue > 39;
    $(`#decrement-months`).prop('disabled', minusDisabled);
    $(`#increment-months`).prop('disabled', plusDisabled);
}

// Ensure proper enabling/disabling
handleEnableDisableMonths();

// Check enable/disable every time the input is changed
$('.months_input').change(function () {
    handleEnableDisableMonths();
});

// Increment quantity
$('.increment-months').click(function (e) {
    e.preventDefault();
    let currentValue = parseInt($('#id_months').val());
    $('#id_months').val(currentValue + 1);
    handleEnableDisableMonths();
});

// Decrement quantity
$('.decrement-months').click(function (e) {
    e.preventDefault();
    let currentValue = parseInt($('#id_months').val());
    $('#id_months').val(currentValue - 1);
    handleEnableDisableMonths();
});



// QUANTITY PART
// Disable +/- buttons outside 1-40 range
function handleEnableDisable() {
    let currentValue = parseInt($(`#id_qty`).val());
    let minusDisabled = currentValue < 2;
    let plusDisabled = currentValue > 39;
    $(`#decrement-qty`).prop('disabled', minusDisabled);
    $(`#increment-qty`).prop('disabled', plusDisabled);
}

// Ensure proper enabling/disabling of all inputs on page load
handleEnableDisable();

// Check enable/disable every time the input is changed
$('.qty_input').change(function () {
    handleEnableDisable();
});

// Increment quantity
$('.increment-qty').click(function (e) {
    e.preventDefault();
    let currentValue = parseInt($('#id_qty').val());
    $('#id_qty').val(currentValue + 1);
    handleEnableDisable();
});

// Decrement quantity
$('.decrement-qty').click(function (e) {
    e.preventDefault();
    let currentValue = parseInt($('#id_qty').val());
    $('#id_qty').val(currentValue - 1);
    handleEnableDisable();
});