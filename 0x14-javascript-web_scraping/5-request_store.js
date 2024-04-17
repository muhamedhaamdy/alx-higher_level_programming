#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const fileName = process.argv[3];

request.get(url, (error, response, body) => {
  if (error || response.statusCode !== 200) {
    console.error('Error:', error || `Status code: ${response.statusCode}`);
    return;
  }
  try {
    fs.writeFileSync(fileName, body, 'utf8');
  } catch (err) {
    console.error('Error:', err);
  }
});
