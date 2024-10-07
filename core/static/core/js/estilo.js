$(document).ready(function(){
    $('.slider').slick({
        infinite: true, // Permite que el carrusel sea infinito
        slidesToShow: 3, // Muestra 3 noticias al mismo tiempo (ajústalo según el tamaño de la pantalla)
        slidesToScroll: 1, // Desplaza una noticia a la vez
        autoplay: true, // Activa el autoplay
        autoplaySpeed: 3000, // Cambia cada 3 segundos
        arrows: true, // Muestra las flechas de navegación
        dots: true, // Agrega indicadores (dots) en la parte inferior
        responsive: [
            {
                breakpoint: 1024, // Para pantallas medianas (tablets)
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 1,
                }
            },
            {
                breakpoint: 600, // Para pantallas pequeñas (móviles)
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }
        ]
    });
});