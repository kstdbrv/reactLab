

const block = document.querySelector('.numbers')

function elementInViewport2(el) {
  var top = el.offsetTop;
  var left = el.offsetLeft;
  var width = el.offsetWidth;
  var height = el.offsetHeight;

  while(el.offsetParent) {
    el = el.offsetParent;
    top += el.offsetTop;
    left += el.offsetLeft;
  }

  return (
    top < (window.pageYOffset + window.innerHeight) &&
    left < (window.pageXOffset + window.innerWidth) &&
    (top + height) > window.pageYOffset &&
    (left + width) > window.pageXOffset
  );
}

document.addEventListener('scroll', event => {
  if (elementInViewport2(block)) {
    setTimeout(function(){
      odometer_0.innerHTML = 10;
    }, 100);

    setTimeout(function(){
      odometer_1.innerHTML = 650;
    }, 100);

    setTimeout(function(){
      odometer_2.innerHTML = 300;
    }, 100);

    setTimeout(function(){
      odometer_3.innerHTML = 320;
    }, 100);

    setTimeout(function(){
      odometer_4.innerHTML = 48;
    }, 100);

    setTimeout(function(){
      odometer_5.innerHTML = 43;
    }, 100);
  }
})

