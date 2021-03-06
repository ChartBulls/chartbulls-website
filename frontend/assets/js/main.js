'use strict';

var userId = null;
var accounts = [];

var accountList = [
    'Coinbase', 
    'GDAX', 
    'Binance',
    'Bittrex',
    'BitMex',
    'KuCoin',
    'Robinhood',
    'TD Ameritrade',
    'Vanguard',
    'Fidelity',
    'ETrade',
    'Charles Schwab',
    'Betterment',
    'Acorns',
    'Wealthfront',
    'Wells Fargo',
    'Chase',
    'Bank of America',
    'Citibank',
    'USAA',
    'Other'
];

var ajaxSettings = {
    type:        'POST',
    contentType: 'application/json; charset=utf-8'
};

$(function() {
    $.ajaxSetup(ajaxSettings);
});

function scrollDown() {
    window.location.href = '#get-early-access'; 
    $('#input-email-footer').focus();
}

function errorAlert(type, msg) {
    $('#alert-text-' + type).html(msg);
    $('#alert-' + type).removeAttr('hidden');
    $('#alert-' + type).show();
    $('#alert-' + type).fadeTo(0, 1);
    setTimeout(() => $('#alert-' + type).fadeTo(700, 0).slideUp(700, function() { $(this).attr('hidden'); }), 2000);
    var html = '<span class="button-text"> Get Early Access </span><i class="fas fa-paper-plane"></i>';
    loadBtn('validate-btn-' + type, false, html);
}

function loadBtn(div, disable, msg) {
    $('#' + div).html(msg);
    $('#' + div).prop('disabled', disable);
}

function validate(type) {
    loadBtn('validate-btn-' + type, true, 'Loading...');

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
            userId = response;
            accounts = [];

            $('#input-email-' + type).val('');
            $('#accounts-title').hide();
            $('#accounts-table').hide();
            $('#my-modal').modal({ 
                backdrop: 'static', 
                keyboard: false 
            });
            $('#input-account').autocomplete({
                source: accountList
            });
            $('#input-account').keypress(function(e) {
                if(e.which == 13) {
                    addAccount();
                }
            });            
            var html = '<span class="button-text"> Get Early Access </span><i class="fas fa-paper-plane"></i>';
            loadBtn('validate-btn-' + type, false, html);    
            loadBtn('submit-btn', true, 'Submit');
        },
        error: function(response) {
            if (response.responseText == 'Duplicate') {
                errorAlert(type, 'This email address is already registered.');
            } else {
                errorAlert(type, 'Unable to subscribe this email address.');
            }
        }
    });
}

function addAccount() {
    var details = $('#input-account').val();

    if (details) {
        accounts.push({
            type:    '',
            details: details
        });
        showAccounts();
        $('#input-account').val('');
        $('#input-account').focus();
    }
}

function removeAccount(index) {
    accounts.splice(index, 1);
    showAccounts();
}

function showAccounts() {
    $('#accounts-table-body').html('');
    
    accounts.forEach(function(account, i) {
        var tr = '<tr> \
                    <td>' + account.details + '</td> \
                    <td class="text-right"> \
                        <button class="btn btn-danger" type="button" onclick="removeAccount(' + i + ')"> \
                            Remove \
                        </button> \
                    </td> \
                  </tr>';

        $('#accounts-table-body').append(tr);        
    });

    if (accounts.length > 0) {
        $('#accounts-title').show();
        $('#accounts-table').show();
        $('#submit-btn').prop('disabled', false);
    } else {
        $('#accounts-title').hide();
        $('#accounts-table').hide();
        $('#submit-btn').prop('disabled', true);
    }
}

function submitAccounts() {
    loadBtn('submit-btn', true, 'Loading...');

    accounts.forEach(function(account, i) {
        var parameters = JSON.stringify({
            'account_type': account.type,
            'details':      account.details,
            'user_id':      userId
        });

        $.ajax({
            url: 'api/v1/accounts',
            data: parameters,
            success: function(response) {
                if (i == accounts.length - 1) {
                    $('#my-modal').modal('hide');
                    $('.alert-jumbotron-success').removeAttr('hidden');
                    $('.alert-jumbotron-success').show();
                    $('.alert-jumbotron-success').fadeTo(0, 1);
                    setTimeout(() => $('.alert-jumbotron-success').fadeTo(700, 0).slideUp(700, function() { $(this).attr('hidden'); }), 2000);
                }
            },
            error: function(response) {                
                $('#alert-modal').removeAttr('hidden');
                $('#alert-modal').show();
            }
        });
    }); 
}