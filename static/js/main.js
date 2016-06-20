$(function() {
    $('#button').click(function() {
        var name = $('#name-box').val();
        $.ajax({
            url: '/sayHello',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                var jsonResponse = $.parseJSON(response);
                $('#hello-mr').html(jsonResponse.hello);
            },
            error: function(error) {
            }
        });
    });
});
