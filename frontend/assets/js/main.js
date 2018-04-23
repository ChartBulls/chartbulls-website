'use strict';

var ajaxSettings = {
    type: 'POST',
    contentType: 'application/json; charset=utf-8'
};

$(function() {
    $.ajaxSetup(ajaxSettings);
});

function subscribe() {
    var email = $('#input-email').val().trim();

    if (email) {
        var parameters = JSON.stringify({
            'email': email
        });

        $.ajax({
            url: 'api/v1/subscribe',
            data: parameters,
            success: function(data) {
                console.log('success');
                console.log(data);
                $('#my-modal').modal('show');
            },
            error: function(data) {
                console.log('error');
                console.log(data);
            }
        });
    } else {
        console.log('email is empty');
    }    
}