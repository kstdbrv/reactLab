const menuItems = document.querySelectorAll('.info-item')

function menuItemsHandler (item) {
    const ul = item.querySelector('.info-drop-ul')
    const svg = item.querySelector('svg')

    if (item == menuItems[1])  {
        menuItems[0].classList.toggle('non-visable')
        item.classList.toggle('info-item-top-web')
    } else {
        menuItems[1].classList.toggle('non-visable')
        item.classList.toggle('info-item-top')
    }
    ul.classList.toggle('visable')
    svg.classList.toggle('non-visable')
}

menuItems.forEach(item => item.addEventListener('click', () => menuItemsHandler(item)))



let cords = ['scrollX','scrollY'];
// Перед закрытием записываем в локалсторадж window.scrollX и window.scrollY как scrollX и scrollY
window.addEventListener('unload', e => cords.forEach(cord => localStorage[cord] = window[cord]));
// Прокручиваем страницу к scrollX и scrollY из localStorage (либо 0,0 если там еще ничего нет)
window.scroll(...cords.map(cord => localStorage[cord]));



// checkbox

function checkboxHandler(item) {
    if (item.checked) {
        document.querySelector('.left').style.display='none';
        if (item.id == 'menu__mobile_toggle_internet') {
            input[0].parentNode.style.marginTop='60px';
            input[1].parentNode.style.display='none';
        } else {
            input[1].parentNode.style.marginTop='60px';
            input[0].parentNode.style.display='none';
        };
        
    } else {
        input.forEach(item => item.parentNode.style.display='', item.parentNode.style.marginTop='')
        document.querySelector('.left').style.display=''
    };
};

const input = document.querySelectorAll('.menu_mobile input[type=checkbox]')

input.forEach(item => item.addEventListener('change', () => checkboxHandler(item)))