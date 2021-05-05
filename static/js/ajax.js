

document.getElementById('fav_icon').addEventListener('click', getFavValue);
// document.getElementById('disab_status').addEventListener('onchange', getDisabValue);

function getFavValue(e){
    e.preventDefault();
    var fvalue= document.getElementById('fav_icon').value;
    console.log(fvalue);

    var xhr = new XMLHttpRequest();
    
    xhr.open('GET', 'add_favourite?fid='+ fvalue, true);
    xhr.onload = function(){
        // document.getElementById('t_text').classList = this.responseText
        let res1 = this.responseText;
        if(res1 == "True"){
            let fvIcon = document.getElementById('fvIcon')
            fvIcon.classList.add('fas')
            fvIcon.classList.remove('far')
            document.getElementById('t_text').innerHTML = 'Added to Favourite List. Click to remove'

        }
        else{
            fvIcon.classList.add('far')
            fvIcon.classList.remove('fas')
            document.getElementById('t_text').innerHTML = 'Click to ad in Favourite list'


        }
        
    }
    xhr.send();
}



// function loadDoc() {
//     var xhttp = new XMLHttpRequest();
//     xhttp.onreadystatechange = function() {
//       if (this.readyState == 4 && this.status == 200) {
//        document.getElementById("demo").innerHTML = this.responseText;
//       }
//     };
//     xhttp.open("GET", "ajax_info.txt", true);
//     xhttp.send();
//   }