if (document.documentElement.clientWidth < '480') {
    jQuery(document).ready(function($){
        $('.center').slick({
            centerMode: true,
            centerPadding: '0px',
            slidesToShow: 1,
            nextArrow: '<button class="sl-btn next">ᐳ</button>',
            prevArrow: '<button class="sl-btn prev">ᐸ</button>',
          });
      });
    
} else {
    jQuery(document).ready(function($){
        $('.center').slick({
            centerMode: true,
            centerPadding: '0px',
            slidesToShow: 3,
            nextArrow: '<button class="sl-btn next">ᐳ</button>',
            prevArrow: '<button class="sl-btn prev">ᐸ</button>',
          });
      });
}



