const options = {
	method: 'GET',
	headers: {
		'X-User-Agent': 'desktop',
		'X-Proxy-Location': 'US',
		'X-RapidAPI-Key': '07269ea256msh32e98b922681710p1e66b1jsn0ab0748aa57f',
		'X-RapidAPI-Host': 'google-search3.p.rapidapi.com'
	}
};



document.addEventListener("DOMContentLoaded", function () {
    let text = "";
    let query ='https://google-search3.p.rapidapi.com/api/v1/search/q=';

    document.getElementById('question').onchange = function () {
        text = this.value;
        query = query+text;
        fetch(query, options)
            .then(response => response.json())

            .then(response => {
                document.getElementById('result1').innerHTML = response.answers[0];
                document.getElementById('result2').innerHTML = response.answers[1];
                document.getElementById('result3').innerHTML = response.answers[2];
                document.getElementById('result4').innerHTML = response.answers[3];
            })
            .then(response => console.log(response))
            .catch(err => console.error(err));

        query = "https://google-search3.p.rapidapi.com/api/v1/search/q="
        //document.getElementById('hello').innerHTML = text;
    }

});

