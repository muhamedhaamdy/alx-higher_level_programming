#!/usr/bin/node

const fileName = process.argv.slice(2)[0];
const fs = require('fs');

try {
  const data = fs.readFileSync(fileName, 'utf8');
  console.log(data);
} catch (err) {
  console.error('Error:', err);
}
