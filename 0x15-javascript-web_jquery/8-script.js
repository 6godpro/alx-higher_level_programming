$(document).ready(function() {
    const url = "https://swapi-api.alx-tools.com/api/films/?format=json"
    fetch(url).then(res => res.json())
    .then(res => {
        for (movie of res['results'])
            $("UL#list_movies").append(`<li>${movie['title']}</li>`)            
    });
});
