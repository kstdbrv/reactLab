
jQuery(document).ready(function(){
    $('.slider_1').slick({
        dots: true,
        dotsClass: 'sl-dots',
        infinite: true,
        speed: 300,
        autoplay: true,
        autoplaySpeed: 1500,
        slidesToShow: 1,
        adaptiveHeight: true,
        arrows: false
      });
      $('.slider_2').slick({
        dots: false,
        infinite: true,
        arrows: false,
        speed: 300,
        slidesToShow: 3,
        adaptiveHeight: true,
        arrows: true,
        nextArrow: '<button class="sl-btn next">ᐳ</button>',
        prevArrow: '<button class="sl-btn prev">ᐸ</button>',
        responsive: [{
          breakpoint: 976,
          settings: {
            slidesToShow: 2,
            slidesToScroll: 1,
            infinite: true,
            dots: false
          }
        }, {
          breakpoint: 768,
          settings: {
          slidesToShow: 2,
          slidesToScroll: 1,
          infinite: true,
          dots: false,
          arrows: false,
        }}]
      });
    
  });



