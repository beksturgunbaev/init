$(document).ready(function() {
    //   Burger menu:
    var div = $(".menu");
    var menu = $('.burger-menu');
    var menuLink = $('.menu--item');

    menu.click(function() {
        div.toggleClass('active');
    });
    $('body').click(function(e) {
        if(!menu.is(e.target) && !div.is(e.target)) {
            div.removeClass('active');
        }
    });
    menuLink.click(function() {
        div.removeClass('active');
    });


    // Click button "more":
    var moreBtn = $('.more-link');
    var moreModal = $('.more-modal');

    moreBtn.click(function() {
        moreModal.toggleClass("show");
    });
    $('body').click(function(e) {
        if(!moreBtn.is(e.target) && !moreModal.is(e.target)) {
            moreModal.removeClass("show");
        }
    });


    //   Скролл при нажатии на меню:
    $('#about--menu').on("click", function(e){
        e.preventDefault();
            var top = $("#about").offset().top - 83;
        $('html,body').animate({
            scrollTop: top
        }, 700);
    });
    $('#students--menu').on("click", function(e){
        e.preventDefault();
            var top = $("#students").offset().top - 83;
        $('html,body').animate({
            scrollTop: top
        }, 700);
    });
    $('#contacts--menu').on("click", function(e){
        e.preventDefault();
            var top = $("#contacts").offset().top - 83;
        $('html,body').animate({
            scrollTop: top
        }, 700);
    });
    $('#teachers-link').on("click", function(e){
        e.preventDefault();
            var top = $("#teachers").offset().top - 83;
        $('html,body').animate({
            scrollTop: top
        }, 700);
    });
    //  При нажатии на кнопку "Получить консультацию":
    $('.get--info--btn').click(function() {
        $('.modal--form').addClass('active');
        $('body').css('overflow', 'hidden');
    });
    $('.close--btn').click(function() {
        $('.modal--form').removeClass('active');
        $('body').css('overflow', 'auto');
    });

    // Наши выпускники (слайдер):
    $(".students--container").slick({
        infinite: true,
        dots: true,
        arrow: true,
        slidesToShow: 5,
        slidesToScroll: 1,
        adaptiveHeight: true,
        responsive: [
            {
                breakpoint: 991,
                settings: {
                    slidesToShow: 4
                }
            },
            {
                breakpoint: 767,
                settings: {
                    slidesToShow: 3
                }
            },
            {
                breakpoint: 576,
                settings: {
                    slidesToShow: 2
                }
            }
        ]
    });
});