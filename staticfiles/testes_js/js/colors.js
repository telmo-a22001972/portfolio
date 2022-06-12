document.addEventListener('DOMContentLoaded', function (){

   document.querySelectorAll('button').forEach(button => {
       button.onclick = () => {
           document.querySelector('#hello').style.color = button.dataset.color;
       }
   })


})