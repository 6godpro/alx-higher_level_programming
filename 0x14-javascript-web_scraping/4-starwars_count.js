#!/usr/bin/node
const request = require('request');
request.get(`${process.argv[2]}`, (err, res, body) => {
  err && console.log(err);
  let count = 0;
  for (const ele of JSON.parse(body).results) {
    for (const people of ele.characters) {
      people.endsWith('18/') && count++; // count character with ID 18.
    }
  }
  console.log(count);
});
