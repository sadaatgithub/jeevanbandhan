const hamBurger = document.querySelector('#burger-menu')
const showNav = document.querySelector('.menu-list')
const logInbtn = document.querySelector('#log-in-btn')
const signUpbtn = document.querySelector('#sign-up-btn')
const loginClose = document.querySelector('#login-close')
const registerClose = document.querySelector('#register-close')
const loginBox = document.querySelector('.log-in-box')
const signUpBox = document.querySelector('.register-here')
const popUpdiv = document.querySelector('.popup-background')





hamBurger.addEventListener('click', () => {
    // console.log('clicked')
    showNav.classList.toggle('show')
    signUpBox.classList.remove('show')
    loginBox.classList.remove('show')


})
if (logInbtn != null ) {
    logInbtn.addEventListener('click', () =>{
    // console.log('clicked1')
    loginBox.classList.add('show')
    signUpBox.classList.remove('show')
    popUpdiv.classList.add('show')
    
  })
}
if (signUpbtn != null){
signUpbtn.addEventListener('click', () =>{
    // console.log('clicked2')
    signUpBox.classList.add('show')
    loginBox.classList.remove('show')
    popUpdiv.classList.add('show')


})
}
if (loginClose != null){
loginClose.addEventListener('click', () =>{
    loginBox.classList.toggle('show')
    popUpdiv.classList.remove('show')


})
}
if (registerClose != null){
registerClose.addEventListener('click', () =>{
    signUpBox.classList.toggle('show')
    popUpdiv.classList.remove('show')


})
}

// document.onclick = function(e){
//     if(e.target.id !== 'login-close'){
//         loginBox.classList.remove('show')
//         console.log('clicked window')

//     }
// }



