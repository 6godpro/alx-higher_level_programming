#!/usr/bin/node
const fs = require('fs');
const request = require('request');
request.get(`${process.argv[2]}`, (err, res, body) => {
  err && console.log(err);
  fs.writeFileSync(process.argv[3], body, 'utf-8');
});
