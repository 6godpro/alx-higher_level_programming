#!/usr/bin/node
// Displays the first argument passed to it on the console.

if (process.argv.slice(2, 3).join() === '') {
  console.log('No argument');
} else {
  console.log(process.argv.slice(2, 3).join());
}
