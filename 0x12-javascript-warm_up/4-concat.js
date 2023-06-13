#!/usr/bin/node
// Displays two arguments passed to it, in the following format: “ is ”

const args = process.argv.slice(2, 4);

console.log(args[0] + ' is ' + args[1]);
