#!/usr/bin/node

exports.esrever = function (list) {
  let len = list.length;
  return list.map((element) => list[--len]);
};
