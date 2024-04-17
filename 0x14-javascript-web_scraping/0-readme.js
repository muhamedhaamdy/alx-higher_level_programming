#!/usr/bin/node

const file_name = process.argv.slice(2)[0];
const fs = require('fs');

try {
    const data = fs.readFileSync(file_name, 'utf8');
    console.log(data);
} catch (err) {
    console.error('Error:', err);
}

