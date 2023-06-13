#!/usr/bin/node
// Computes and prints the factorial of a number.

function factorial (n) {
  if (n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}

const arg = process.argv.slice(2, 3).join();

if (Number.isNaN(Number(arg)) || arg === '') {
  console.log(1);
} else {
  console.log(factorial(Number(arg)));
}
