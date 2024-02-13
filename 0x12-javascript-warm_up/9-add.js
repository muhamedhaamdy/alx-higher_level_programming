#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const argv = process.argv;

if (isNaN(parseInt(argv[2])) || isNaN(parseInt(argv[3]))) {
  console.log('NaN');
} else {
  console.log(add(parseInt(argv[2]), parseInt(argv[3])));
}
