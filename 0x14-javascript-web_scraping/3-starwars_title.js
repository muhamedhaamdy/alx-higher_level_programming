#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv.slice(2)[0];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } const data = JSON.parse(body);
  console.log(data.title);
});
