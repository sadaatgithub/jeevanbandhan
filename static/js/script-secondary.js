const toggles = document.querySelectorAll('.faq-toggle')


toggles.forEach(toggle => {
    toggle.addEventListener('click', () => {
        toggle.parentNode.classList.toggle('active')
    })
})

const closeAlert = document.querySelector('#alert-close')
const alertBox = document.querySelector('#alert')
if (alertBox != null ) { //make sure we don't run this script if the slideshow is not present

if(alertBox.classList.contains ="success"){
    setTimeout(() => {
        alertBox.classList.add('hide')
    }, 5000);
}

closeAlert.addEventListener('click', () =>{

        alertBox.classList.add('hide')
        
  
})
}






