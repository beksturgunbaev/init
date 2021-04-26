$(document).ready(function() {
//   Burger menu:
$('.burger-menu').click(function() {
    $('.menu').addClass('active');
});
$('.menu--item').click(function() {
    $('.menu').removeClass('active');
});

// Click вне элемента меню:
    jQuery(function($){
        $(document).mouseup(function (e) {
            var div = $(".menu");
            if (!div.is(e.target)
                && div.has(e.target).length === 0) { 
                div.removeClass('active');
            }
        });
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