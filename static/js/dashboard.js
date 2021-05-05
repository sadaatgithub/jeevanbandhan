const DbMenu = document.querySelector('#dashboard')
const DbClose = document.querySelector('#dashboard-close-btn')
const DbOpen = document.querySelector('#bashboard-btn')

document.onclick = function(e){
    if(e.target.id !== 'bashboard-btn'){
    DbMenu.classList.remove('active')
            // console.log('clicked')

    }
}
if (DbOpen != null ) {

DbOpen.addEventListener('click', () =>{
    DbMenu.classList.toggle('active')
    // showNav.classList.toggle('show')
    // console.log(e.target.id)


})

DbClose.addEventListener('click', () => {
    DbMenu.classList.toggle('active')

})
}