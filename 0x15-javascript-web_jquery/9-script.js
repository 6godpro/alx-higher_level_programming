$(document).ready(function() {
    fetch("https://fourtonfish.com/hellosalut/?lang=fr")
    .then(res => res.json())
    .then(res => {
        $("DIV#hello").text(res['hello']);
    });
});
