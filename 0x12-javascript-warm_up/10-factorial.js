#!/usr/bin/node

function fac (a) {
  if (a === 1) return 1;
  else return (a * fac(a - 1));
}

const argv = process.argv;

if (isNaN(parseInt(argv[2]))) {
  console.log('1');
} else {
  console.log(fac(parseInt(argv[2])));
}
