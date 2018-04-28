'use strict';

var ajaxSettings = {
    type:        'POST',
    contentType: 'application/json; charset=utf-8'
};

$(function() {
    $.ajaxSetup(ajaxSettings);
});

function errorAlert(type, msg) {
    $('#alert-text-' + type).html(msg);
    $('#alert-' + type).removeAttr('hidden');
    $('#alert-' + type).show();
    $('#alert-' + type).fadeTo(0, 1);
    setTimeout(() => $('#alert-' + type).fadeTo(700, 0).slideUp(700, function() { $(this).attr('hidden'); }), 2000);
}

function validate(type) {
    var email = $('#input-email-' + type).val().trim();

    if (email) {
        subscribe(email, type);
    } else {
        errorAlert(type, 'Please enter your email address.');
    }
}

function subscribe(email, type) {
    var parameters = JSON.stringify({
        'email': email
    });

    $.ajax({
        url: 'api/v1/subscribe',
        data: parameters,
        success: function(response) { 
            $('#my-modal').modal('show');           
            console.log('success : ' + type);
            console.log(response);
        },
        error: function(response) {
            console.log(response);

            if (response.responseText == 'Duplicate') {
                errorAlert(type, 'This email address is already registered.');
            } else {
                errorAlert(type, 'Unable to subscribe this email address.');
            }
        }
    });
}