$(document).ready(function () {
    $('.m-form').submit(function (event) {
        event.preventDefault();

        message = $('.flash');
        message.text("查找中...");
        sno = $('.m-input').val();
        img = $('.avatar');
        $.post("/search", {'sno': sno},
            function (data) {
                message.text("");
                if (data.status == "error") {
                    message.text(data.message);
                } else if (data.status == "success") {
                    img.css('background-image', 'url(' + data.imgUrl + ')');
                }
            },
        "json");
    });
});
