document.addEventListener('DOMContentLoaded', function (){
    fetch(`https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/3490100.json`)
        .then(response => response.json())
        .then(data => {
            const tmin = data.data[0].tMin;

            document.getElementById('tMin').innerHTML = tmin;
        })
})
