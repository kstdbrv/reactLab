const infoItem1 = document.getElementById('info-item1');
const infoItem2 = document.getElementById('info-item2');
const infoUl1 = document.getElementById('info-ul1')
const infoUl2 = document.getElementById('info-ul2')

infoItem1.onclick = function dropDown() {
    if (infoItem2.classList.contains('non-visable')) {
        return (infoItem2.classList.remove('non-visable') + 
        infoUl1.classList.remove('visable') +
        infoUl1.classList.toggle('non-visable') + 
        infoItem1.classList.remove('info-item-top') + 
        infoItem1.childNodes[1].classList.toggle('non-visable'));
    };
    return (infoItem2.classList.toggle('non-visable') + 
    infoUl1.classList.remove('non-visable') + 
    infoUl1.classList.toggle('visable') +
    infoItem1.classList.toggle('info-item-top') + 
    infoItem1.childNodes[1].classList.remove('non-visable'));
};

infoItem2.onclick = function dropDown2() {
    if (infoItem1.classList.contains('non-visable')) {
        return (infoItem1.classList.remove('non-visable') + 
        infoUl2.classList.toggle('non-visable') + 
        infoUl2.classList.remove('visable') +
        infoItem2.classList.remove('info-item-top-web') + 
        infoItem2.childNodes[1].classList.toggle('non-visable'));
    };
    return (infoItem1.classList.toggle('non-visable') + 
    infoUl2.classList.remove('non-visable') + 
    infoUl2.classList.toggle('visable') +
    infoItem2.classList.toggle('info-item-top-web') + 
    infoItem2.childNodes[1].classList.remove('non-visable'));
};

let cords = ['scrollX','scrollY'];
// Перед закрытием записываем в локалсторадж window.scrollX и window.scrollY как scrollX и scrollY
window.addEventListener('unload', e => cords.forEach(cord => localStorage[cord] = window[cord]));
// Прокручиваем страницу к scrollX и scrollY из localStorage (либо 0,0 если там еще ничего нет)
window.scroll(...cords.map(cord => localStorage[cord]));