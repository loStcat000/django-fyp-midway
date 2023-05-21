$(document).ready(function() {
    $(window).scroll(function() {
        if ($(this).scrollTop() > 50) {
            $('.navbar').addClass('navbar-scroll');
        } else {
            $('.navbar').removeClass('navbar-scroll');
        }
    });
});