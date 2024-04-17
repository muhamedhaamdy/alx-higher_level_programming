#!/usr/bin/node

const fileName = process.argv.slice(2)[0];
const data = process.argv.slice(3)[0];
const fs = require('fs');

try {
  fs.writeFileSync(fileName, data, 'utf8');
} catch (err) {
  console.error('Error:', err);
}
