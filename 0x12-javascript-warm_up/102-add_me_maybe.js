#!/usr/bin/node
// Increments and calls a function.

exports.addMeMaybe = function (x, func) {
  func(++x);
};
