const icons = document.querySelectorAll('.icon')
const discr = document.querySelectorAll('.stages__icons_discr p')

icons.forEach((icon, index) => icon.addEventListener('click', () => {
    document.querySelector('.current').classList.remove('current'),
    document.querySelector('.visable').classList.remove('visable'),
    icon.classList.toggle('current'),
    discr[index].classList.toggle('visable')
}))
