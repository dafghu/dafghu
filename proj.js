document.addEventListener('DOMContentLoaded', function () {
  const swiper = new Swiper('.textSlider', {
    slidesPerView: 1,      // всегда один слайд
    spaceBetween: 20,      // расстояние между слайдами (при переключении)
    loop: true,            // зацикливание
    autoplay: {
      delay:100000,         // автопереключение через 4 секунды (можно отключить)
      disableOnInteraction: false,
    },
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
    },
    scrollbar: {
      el: '.swiper-scrollbar',
      hide: true,
    },
    speed: 600,            // скорость анимации переключения
  });
});