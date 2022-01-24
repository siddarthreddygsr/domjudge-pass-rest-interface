jQuery(document).ready(function ($) {
    $('.search-box').on('keyup', function () {
        var searchTerm = $(this).val().toLowerCase();
        // text.innerHTML = searchTerm;
        // console.log(searchTerm);
        data = {
            searchTerm: searchTerm
        }
        $.ajax({
            url: '/search_unique_email/',
            type: 'POST',
            data: data,
            dataType: 'json',
            success: function (resp) {
                console.log(resp[0]);

                respin = ""
                dummy = ""
                for (let i = 0; i < resp.length; i++) 
                {
                    respin += "<li><h2>" + resp[i].email + "</h2></li>";
                    dummy = resp[i].email+ "," + dummy;
                }
                suggestions.innerHTML = respin;
                text.innerHTML = dummy;
            }
        })
    });

});