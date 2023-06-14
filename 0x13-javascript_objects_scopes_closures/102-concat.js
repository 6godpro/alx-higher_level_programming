#!/usr/bin/node
const fs = require('fs');

const args = process.argv.slice(2);
const contentA = fs.readFileSync(args[0]);
const contentB = fs.readFileSync(args[1]);
fs.writeFileSync(args[2], contentA + contentB);
