// JavaScript script that fetches the character name from this URL: https://swapi-api.hbtn.io/api/people/5/?format=json using jquery api 

$.getJSON('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
    $('DIV#character').html(data['name']);
});
