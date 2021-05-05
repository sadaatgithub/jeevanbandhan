const dType = document.querySelector('#disab_type');
const dCent = document.querySelector('#disab_cent');
const advSearch = document.querySelector('#advSearch')







if (dType != null ) {
var dValue= document.getElementById('disab_status').value;
console.log(dValue)
if(dValue == "Yes"){
    dType.style.display = "flex";
    dCent.style.display = "flex";


}
function getDisabValue(){
            var dValue= document.getElementById('disab_status').value;
            console.log(dValue);
            
                if(dValue == "Yes"){
                    dType.style.display = "flex"
                    dCent.style.display = "flex"     
                }
                else{
                    dType.style.display = "none"
                    dCent.style.display = "none"

                }


}
}