#!/usr/bin/node

const argv = process.argv;

if (isNaN(parseInt(argv[2]))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(argv[2]); i++) {
    for (let j = 0; j < parseInt(argv[2]); j++) {
      process.stdout.write('X');
    } console.log();
  }
}
