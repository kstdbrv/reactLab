const choisesItem = document.querySelector('.choises__item')
const choisesSubcategoryItem = document.querySelector('.choises__subcategory-item')

const category = document.querySelectorAll('.quiz__label input')
const subcategory = document.querySelectorAll('.choises__subcategory-item label')
const btn = document.querySelector('.quiz__btn')
const contactInfo = document.querySelector('.choises__contact-info')

const internet = Array.prototype.slice.call(subcategory).slice(0,5)
const web = Array.prototype.slice.call(subcategory).slice(5,11)

contactInfo.style.display='none'
subcategory.forEach(item => item.style.display='none')

function createInternetSubcategoriesList() {
    internet.forEach(item => item.style.display='')
    web.forEach(item => item.style.display='none')
    choisesItem.style.display='none'
}

function createWebSubcategoriesList() {
    web.forEach(item => item.style.display='')
    internet.forEach(item => item.style.display='none')
    choisesItem.style.display='none'
}


category.forEach((item) => item.addEventListener('change', () => {

    if (item.parentElement.innerText == 'интернет-маркетинг') {
        btn.onclick = createInternetSubcategoriesList
    }
    if (item.parentElement.innerText == 'веб-разработка') {
        btn.onclick = createWebSubcategoriesList
    }

}))

btn.addEventListener('click', () => {
    
    if (choisesItem.style.display == 'none') {
        choisesSubcategoryItem.style.display='none'
        contactInfo.style.display=''
        btn.setAttribute('type', 'submit')
    }
})