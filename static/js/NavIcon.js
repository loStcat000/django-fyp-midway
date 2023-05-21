$(document).ready(function() {
    $('.profile-icon > a').on('click', function() {
        var dropdown = $(this).next('.dropdown-menu');
        $('.dropdown-menu').not(dropdown).hide(); // hide any open dropdowns except for the clicked one
        dropdown.toggle();
    });
});