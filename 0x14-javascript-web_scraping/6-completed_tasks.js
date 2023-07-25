#!/usr/bin/node
const request = require('request');
const completed = {};
request.get(process.argv[2], (err, res, body) => {
  if (!err) {
    const todos = JSON.parse(body);
    todos.forEach((task) => {
      if (task.completed) {
        if (completed[task.userId] === undefined) {
          completed[task.userId] = 1;
        } else {
          completed[task.userId] += 1;
        }
      }
    });
    console.log(completed);
  }
});
