# **JavaScript - Web Scraping**

In this project, I continued practicing how to work with JSON data retrieved using `fetch` and `request` APIs. I also practiced reading and writing to files using the `fs` module.

## TASKS :book:

### [0. Readme](./0-readme.js)
Write a script that reads and prints the content of a file.

* The first argument is the file path
* The content of the file must be read in utf-8
* If an error occurred during the reading, print the error object

### [1. Write me](./1-writeme.js)
Write a script that writes a string to a file.

* The first argument is the file path
* The second argument is the string to write
* The content of the file must be written in utf-8
* If an error occurred during while writing, print the error object

### [2. Status code](./2-statuscode.js)
Write a script that display the status code of a GET request.

* The first argument is the URL to request (GET)
* The status code must be printed like this: code: `<status code>`
* You must use the module request

### [3. Star wars movie title](./3-starwars_title.js)
Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.

* The first argument is the movie ID
* You must use the Star wars API with the endpoint https://swapi-api.alx-tools.com/api/films/:id
* You must use the module request