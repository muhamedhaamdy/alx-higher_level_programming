#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error || response.statusCode !== 200) {
    console.error('Error:', error || `Status code: ${response.statusCode}`);
    return;
  }
  const data = JSON.parse(body);
  let dict = {};
  for (obj of data) {
    if (!dict[obj.userId]) {
        dict[obj.userId] = 0;
    } if (obj.completed)
    dict[obj.userId]++;
    }
  console.log(dict);
});
