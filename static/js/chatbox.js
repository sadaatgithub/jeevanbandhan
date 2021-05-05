const chatboxClose = document.querySelector('#chat-times')
const chatbox = document.querySelector('#chatbox')
const chatStart = document.querySelector('.fa-comments')

chatboxClose.addEventListener('click', ()=>{
        chatbox.classList.add('hide')
        console.log('clicked 3')
})

chatStart.addEventListener('click', ()=>{
    chatbox.classList.remove('hide')

})