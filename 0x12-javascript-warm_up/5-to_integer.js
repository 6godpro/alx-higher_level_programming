#!/usr/bin/node
// Displays the first argument if it can be converted to an integer.

const arg = process.argv.slice(2, 3).join();

if (Number.isNaN(Number(arg))) {
  console.log('Not a number');
} else {
  console.log('My number:', Number(parseInt(arg)));
}
