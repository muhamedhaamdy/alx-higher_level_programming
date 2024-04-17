#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
let count = 0;
let completedRequests = 0;

// Loop to make requests for films 0 to 6
for (let i = 0; i < 7; i++) {
  makeRequest(url + '/' + i);
}

function makeRequest (url) {
  request(url, function (error, response, body) {
    if (error) {
      console.error(error);
      checkCompletion();
      return;
    }

    try {
      const data = JSON.parse(body);
      if (data.characters && Array.isArray(data.characters) && data.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
        count++;
      }
    } catch (parseError) {
      console.error('Error parsing response body:', parseError);
    }

    checkCompletion();
  });
} function checkCompletion () {
  completedRequests++;
  if (completedRequests === 7) {
    console.log(count);
  }
}
