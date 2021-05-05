const abtBtn = document.querySelector('#abt_me_btn');
const familyBtn = document.querySelector('#abt_family_btn');
const partnerBtn = document.querySelector('#abt_partner_btn');
const abtDiv = document.querySelector('#abt_me');
const familyDiv = document.querySelector('#abt_family');
const partnertDiv = document.querySelector('#abt_partner');

if (abtBtn != null ) {
abtBtn.addEventListener('click', () =>{
    // console.log('abtBtn clicked')
    abtDiv.classList.remove('hidden')
    partnertDiv.classList.add('hidden')
    familyDiv.classList.add('hidden')
    abtBtn.classList.add('active')
    familyBtn.classList.remove('active')
    partnerBtn.classList.remove('active')



})
}
if (familyBtn != null ) {
familyBtn.addEventListener('click', () =>{
    abtDiv.classList.add('hidden')
    familyDiv.classList.remove('hidden')
    partnertDiv.classList.add('hidden')
    familyBtn.classList.add('active')
    abtBtn.classList.remove('active')
    partnerBtn.classList.remove('active')

})
}
if (partnerBtn != null ) {
partnerBtn.addEventListener('click', () =>{
    abtDiv.classList.add('hidden')
    familyDiv.classList.add('hidden')
    familyBtn.classList.remove('active')
    abtBtn.classList.remove('active')
    partnerBtn.classList.add('active')
    partnertDiv.classList.remove('hidden')
})
}