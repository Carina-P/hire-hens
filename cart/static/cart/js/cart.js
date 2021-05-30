// Update quantity on click
$('.update-link').click(function (e) {
    let form = $(this).prev('.update-form');
    form.submit();
});


// Update quantity on click
$('.update-link_rental').click(function (e) {
    let form = $(this).prev('.update-rental-form');
    form.submit();
});

// Update quantity on click
$('.update-link_lg').click(function (e) {
    let form = $(this).prev('.update-form_lg');
    form.submit();
});


// Update quantity on click
$('.update-link_rental_lg').click(function (e) {
    let form = $(this).prev('.update-rental-form_lg');
    form.submit();
});


// Open modal to ask if user realy want to remove item from cart
function openRemoveModal(itemId, name) {
    if (itemId === undefined || itemId === null) {
        console.log(
            "Error in function openRemoveModal, itemId undefined");
        return;
    }
    if (name === undefined || name === null) {
        console.log(
            "Error in function openRemoveModal, name undefined");
        return;
    }

    $('#name').html(name);
    $('#hidden_item').html(`<input type="hidden" name="item_id" value="${itemId}">`);
    $('#modal_remove').modal('show');
}

// Open modal to ask if user realy want to remove item from cart
function openRemoveModalRent(itemId, name, months) {
    if (itemId === undefined || itemId === null) {
        console.log(
            "Error in function openRemoveModal, itemId undefined");
        return;
    }
    if (name === undefined || name === null) {
        console.log(
            "Error in function openRemoveModal, name undefined");
        return;
    }
    if (months === undefined || months === null) {
        console.log(
            "Error in function openRemoveModal, months undefined");
        return;
    }

    $('#name_rent').html(name);
    $('#hidden_item_rent').html(`<input type="hidden" name="item_id" value="${itemId}">
    <input type="hidden" name="months" value="${months}">`);
    $('#modal_remove_rent').modal('show');
}

// Code from Code Institute Boutique Ado
$('.btt-link').click(function (e) {
    window.scrollTo(0, 0);
});


// Code below is inspired from Code Institute Boutique Ado
// BUY PART OF CART
// Disable +/- buttons outside 1-40 range
function handleEnableDisable(itemId) {
    let currentValue = parseInt($(`#id_qty_${itemId}`).val());
    let minusDisabled = currentValue < 2;
    let plusDisabled = currentValue > 39;
    $(`#decrement-qty_${itemId}`).prop('disabled', minusDisabled);
    $(`#increment-qty_${itemId}`).prop('disabled', plusDisabled);
}

// Ensure proper enabling/disabling of all inputs on page load
let allQtyInputs = $('.qty_input');
for (let i = 0; i < allQtyInputs.length; i++) {
    let itemId = $(allQtyInputs[i]).data('item_id');
    handleEnableDisable(itemId);
}

// Check enable/disable every time the input is changed
$('.qty_input').change(function () {
    let itemId = $(this).data('item_id');
    handleEnableDisable(itemId);
});

// Increment quantity
$('.increment-qty').click(function (e) {
    e.preventDefault();
    let closestInput = $(this).closest('.input-group').find('.qty_input')[0];
    let currentValue = parseInt($(closestInput).val());
    $(closestInput).val(currentValue + 1);
    let itemId = $(this).data('item_id');
    handleEnableDisable(itemId);
});

// Decrement quantity
$('.decrement-qty').click(function (e) {
    e.preventDefault();
    let closestInput = $(this).closest('.input-group').find('.qty_input')[0];
    let currentValue = parseInt($(closestInput).val());
    $(closestInput).val(currentValue - 1);
    let itemId = $(this).data('item_id');
    handleEnableDisable(itemId);
});

// RENTAL PART OF CART
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

// LARGER SCREENS
// BUY PART OF CART
// Disable +/- buttons outside 1-40 range
function handleEnableDisableLg(itemId) {
    let currentValue = parseInt($(`#id_qty_lg_${itemId}`).val());
    let minusDisabled = currentValue < 2;
    let plusDisabled = currentValue > 39;
    $(`#decrement-qty_lg_${itemId}`).prop('disabled', minusDisabled);
    $(`#increment-qty_lg_${itemId}`).prop('disabled', plusDisabled);
}

// Ensure proper enabling/disabling of all inputs on page load
let allQtyInputsLg = $('.qty_input_lg');
for (let i = 0; i < allQtyInputsLg.length; i++) {
    let itemId = $(allQtyInputsLg[i]).data('item_id');
    handleEnableDisableLg(itemId);
}

// Check enable/disable every time the input is changed
$('.qty_input_lg').change(function () {
    let itemId = $(this).data('item_id');
    handleEnableDisableLg(itemId);
});

// Increment quantity
$('.increment-qty').click(function (e) {
    e.preventDefault();
    let closestInput = $(this).closest('.input-group').find('.qty_input_lg')[0];
    let currentValue = parseInt($(closestInput).val());
    $(closestInput).val(currentValue + 1);
    let itemId = $(this).data('item_id');
    handleEnableDisableLg(itemId);
});

// Decrement quantity
$('.decrement-qty').click(function (e) {
    e.preventDefault();
    let closestInput = $(this).closest('.input-group').find('.qty_input_lg')[0];
    let currentValue = parseInt($(closestInput).val());
    $(closestInput).val(currentValue - 1);
    let itemId = $(this).data('item_id');
    handleEnableDisableLg(itemId);
});

// RENTAL PART OF CART
// Disable +/- buttons outside 1-40 range
function handleEnableDisableRentalLg(id) {
    let currentValue = parseInt($(`#id_qty_lg_${id}`).val());
    let minusDisabled = currentValue < 2;
    let plusDisabled = currentValue > 39;
    $(`#decrement-qty_lg_${id}`).prop('disabled', minusDisabled);
    $(`#increment-qty_lg_${id}`).prop('disabled', plusDisabled);
}

// Ensure proper enabling/disabling of all inputs on page load
let allQtyInputsRentalLg = $('.qty_input_rental_lg');
for (let i = 0; i < allQtyInputsRentalLg.length; i++) {
    let id = $(allQtyInputsRentalLg[i]).data('id');
    handleEnableDisableRentalLg(id);
}

// Check enable/disable every time the input is changed
$('.qty_input_rental_lg').change(function () {
    let id = $(this).data('id');
    handleEnableDisableRentalLg(id);
});

// Increment quantity
$('.increment-qty_rental').click(function (e) {
    e.preventDefault();
    let closestInput = $(this).closest('.input-group').find('.qty_input_rental_lg')[0];
    let currentValue = parseInt($(closestInput).val());
    $(closestInput).val(currentValue + 1);
    let id = $(this).data('id');
    handleEnableDisableRentalLg(id);
});

// Decrement quantity
$('.decrement-qty_rental').click(function (e) {
    e.preventDefault();
    let closestInput = $(this).closest('.input-group').find('.qty_input_rental_lg')[0];
    let currentValue = parseInt($(closestInput).val());
    $(closestInput).val(currentValue - 1);
    let id = $(this).data('id');
    handleEnableDisableRentalLg(id);
});