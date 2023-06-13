#!/usr/bin/node
// prints x times “C is fun”

const arg = process.argv.slice(2, 3).join();

if (Number.isNaN(Number(arg)) || arg === '') {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < Number(arg); i++) {
    console.log('C is fun');
  }
}
