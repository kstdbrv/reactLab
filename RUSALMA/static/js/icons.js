const icons = document.querySelectorAll('.icon')
const discr = document.querySelectorAll('.stages__icons_discr p')

function choiseCurrentIcon(item, index) {
    document.querySelector('.current').classList.remove('current');
    document.querySelector('.visable').classList.remove('visable');
    item.classList.toggle('current');
    discr[index].classList.toggle('visable');
}



icons.forEach((icon, index) => icon.addEventListener('click', () => choiseCurrentIcon(icon, index)))
   
