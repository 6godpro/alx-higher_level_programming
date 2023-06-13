#!/usr/bin/node
// prints x times “C is fun”

const arg = process.argv.slice(2, 3).join();

if (Number.isNaN(Number(arg)) || arg === '') {
  console.log('Missing size');
} else {
  let square = '';
  for (let i = 0; i < Number(arg); i++) {
    square += 'X';
  }
  for (let i = 0; i < Number(arg); i++) {
    console.log(square);
  }
}
