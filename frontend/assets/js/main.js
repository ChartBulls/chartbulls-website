'use strict';

var ajaxSettings = {
    type:        'POST',
    contentType: 'application/json; charset=utf-8'
};

$(function() {
    $.ajaxSetup(ajaxSettings);
});

function validate(type) {
    var email = $('#input-email-' + type).val().trim();

    if (email) {
        subscribe(email, type);
    } else {
        $('#alert-text-' + type).html('Email address cannot be blank.');
        $('#alert-' + type).removeAttr('hidden');
        setTimeout(() => $('#alert-' + type).fadeTo(700, 0).slideUp(700, function () { $(this).remove(); }), 2000);
    }    
}

function subscribe(email, type) {
    var parameters = JSON.stringify({
        'email': email
    });

    $.ajax({
        url: 'api/v1/subscribe',
        data: parameters,
        success: function(data) {            
            console.log('success : ' + type);
            console.log(data);
            $('#my-modal').modal('show');
        },
        error: function(data) {
            console.log('error : ' + type);
            console.log(data);
        }
    });
}