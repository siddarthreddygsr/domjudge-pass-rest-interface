$("form[name=signup_form]").submit(function(e) {
    var $form = $(this);
    var $error = $form.find('.error');
    var data = $form.serialize();

    $.ajax({
        url: "/user/sign_up/",
        type: "POST",
        data: data,
        dataType: "json",
        success: function(response) {
            console.log(response);
        },
        error: function(response) {
            console.log(response);
            $error.text(response.responseJSON.error).removeClass('error--hidden');
        }
    });
    e.preventDefault();
})