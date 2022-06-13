document.addEventListener('DOMContentLoaded', function () {

    fetch('https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json')
        .then(resp => resp.json())
        .then(data => {
            const tmin = data.data[0].tMin
            const tmax = data.data[0].tMax
            const dia = data.data[0].forecastDate
            document.getElementById('t_min_lisboa').innerHTML = "T. Mínima: " + tmin+"°C"
            document.getElementById('t_max_lisboa').innerHTML = "T. Máxima: " + tmax+"°C"
            document.getElementById('data_lisboa').innerHTML = "Dia: " + dia
    })

    fetch('https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1131200.json')
        .then(resp => resp.json())
        .then(data => {
            const tmin = data.data[0].tMin
            const tmax = data.data[0].tMax
            const dia = data.data[0].forecastDate
            document.getElementById('t_min_porto').innerHTML = "T. Mínima: " + tmin+"°C"
            document.getElementById('t_max_porto').innerHTML = "T. Máxima: " + tmax+"°C"
            document.getElementById('data_porto').innerHTML = "Dia: " + dia
    })

    fetch('https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1080500.json')
        .then(resp => resp.json())
        .then(data => {
            const tmin = data.data[0].tMin
            const tmax = data.data[0].tMax
            const dia = data.data[0].forecastDate
            document.getElementById('t_min_faro').innerHTML = "T. Mínima: " + tmin+"°C"
            document.getElementById('t_max_faro').innerHTML = "T. Máxima: " + tmax+"°C"
            document.getElementById('data_faro').innerHTML = "Dia: " + dia
    })

})