$(document).on('ready', function () {
    $('.slider-for').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        fade: true,
        asNavFor: '.slider-nav'
    });
    $('.slider-nav').slick({
        slidesToShow: 5,
        slidesToScroll: 1,
        asNavFor: '.slider-for',
        dots: false,
        centerMode: true,
        focusOnSelect: true,
        responsive: [
             {
                breakpoint: 992, // Планшеты (меньше 992px)
                settings: {
                    slidesToShow: 4,
                    arrows: false
                }
            },
            {
                breakpoint: 768, // Мобильные (меньше 768px)
                settings: {
                    slidesToShow: 3,
                    arrows: false
                }
            }
        ]
    });
});