$(document).ready(function() {
    console.log('Document loaded');
    // Adding click event to login button
    $('#loginButton').on('click', function() {
        console.log('button clicked')
        // Grab the form values
        let auth_endpoint = $('#apiAuthEndpoint').val();
        let username = $('#username').val();
        let password = $('#passwd').val();

        // Setup the request
        req = $.ajax({
            // The flask endpoint we'll trigger to actually send the request
            url: '/gettoken',
            type: 'POST',
            // The data we want to send into flask
            data: {
                "target": auth_endpoint,
                "headers": {
                    "username": username,
                    "password": password
                }
            }
        });

        // After the call has finished, update the text in the token
        // display area in the html
        req.done(function(data) {
            $('#tokenresult').text(data)
        });

    });
});
