#!/usr/bin/node
// Searches the second biggest integer in the list of arguments.

const args = process.argv.slice(2).map(n => Number(n));
const lenArgs = args.length;

if (lenArgs < 2) {
  console.log(0);
} else {
  console.log(args.sort((a, b) => a - b)[lenArgs - 2]);
}
