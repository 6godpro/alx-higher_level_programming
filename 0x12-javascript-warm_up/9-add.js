#!/usr/bin/node
// Displays the sum of two integers.

function add (a, b) {
  return a + b;
}

const args = process.argv.slice(2, 4);
console.log(add(Number(args[0]), Number(args[1])));
