#!/usr/bin/node
const fs = require('fs');

const fileName = process.argv[2];
fs.readFile(fileName, { encoding: 'utf-8' }, (err, data) => {
  if (err) {
    console.log(`{ Error: ${err.message} 
  errno: ${err.errno},
  code: '${err.code}',
  syscall: '${err.syscall}',
  path: '${err.path}' }`);
  } else {
    console.log(data);
  }
});
