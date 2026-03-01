$(document).ready(function () {
    // Инициализация слайдеров
    $('.slider-for').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: true,
        fade: true,
        asNavFor: '.slider-nav'
    });

    $('.slider-nav').slick({
        slidesToShow: 5,
        slidesToScroll: 1,
        asNavFor: '.slider-for',
        dots: false,
        arrows: true,
        centerMode: true,
        focusOnSelect: true,
        responsive: [
            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 3
                }
            },
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 2
                }
            }
        ]
    });

    // Инициализация модального слайдера
    const $modalSlider = $('.modal-slider');

    $modalSlider.slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: true,
        fade: true,
        infinite: true
    });

    // Обработка клика по большому изображению
    $('.slider-for-item img').on('click', function () {
        const index = $(this).data('index');

        // Переключаем модальный слайдер на нужный слайд
        $modalSlider.slick('slickGoTo', index);
    });

    // Синхронизация при открытии модального окна
    $('#galleryModal').on('shown.bs.modal', function () {
        $modalSlider.slick('setPosition');
    });
});
