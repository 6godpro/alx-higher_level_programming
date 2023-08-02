$(document).ready(function() {
    const url = "https://swapi-api.alx-tools.com/api/people/5/?format=json"
    fetch(url).then(res => res.json())
    .then(res => $("DIV#character").text(res['name']))
});
