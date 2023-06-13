#!/usr/bin/node
// Displays a message depending of the number of arguments passed.

const lenArgv = process.argv.slice(2).length;

if (lenArgv === 0) {
  console.log('No argument');
} else if (lenArgv === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
