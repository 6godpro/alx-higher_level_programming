#!/usr/bin/node
const request = require('request');

// makes a request to a URL and returns a Promise.
function makeRequest (url) {
  return new Promise((resolve, reject) => {
    request.get(url, (err, resp, body) => {
      if (err) {
        reject(err);
      } else {
        resolve(body);
      }
    });
  });
}

// async function to fetch url sequentially from a list.
async function fetchSequentially (urlList) {
  for (const url of urlList) {
    const character = await makeRequest(url);
    console.log(JSON.parse(character).name);
  }
}

request.get(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, (err, res, body) => {
  if (!err) {
    const characters = JSON.parse(body).characters;
    fetchSequentially(characters);
  }
});
