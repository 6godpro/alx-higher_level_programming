#!/usr/bin/node
const request = require('request');
const completed = {};
request.get(process.argv[2], (err, res, body) => {
  err && console.log(err);
  const todos = JSON.parse(body);
  todos.forEach((task) => {
    if (task.completed && completed[task.userId] === undefined) {
      completed[task.userId] = 1;
    } else {
      task.completed && completed[task.userId]++;
    }
  });
  console.log(completed);
});
