let counter = 0;
function count() {
        document.querySelector('h1').innerHTML= `A contagem vai em ${++counter}`;
    }
    document.addEventListener('DOMContentLoaded', function () {
        document.querySelector('button').onclick = count;
    })


