#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
let counter = 0;

request.get(url, (error, response, body) => {
  if (error || response.statusCode !== 200) {
    console.error('Error:', error || `Status code: ${response.statusCode}`);
    return;
  }

  const data = JSON.parse(body);

  data.results.forEach(result => {
    result.characters.forEach(character => {
      if (character === 'https://swapi-api.alx-tools.com/api/people/18/') {
        counter++;
      }
    });
  });

  console.log(counter);
});
