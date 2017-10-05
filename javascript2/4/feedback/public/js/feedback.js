(function ($) {
    $(function () {
        $.ajax({
            url: 'json/cities',
            dataType: 'json',
            success: function (data, textStatus) {
                console.log(data);
                addCities(data);
            }
        });
        $('#drag').click(function () {
            console.log("yeahh");
            $('#cont').toggleClass("isUp", 3000);
            slideToggle( "slow", function() {
            });
        });

    })
})(jQuery);

function addCities(data) {
    var cityname = $('#cityname');
    for(var item of data) {
        var option = "<option value='" + item.city+ "'>";
        cityname.append(option);
    }
}

