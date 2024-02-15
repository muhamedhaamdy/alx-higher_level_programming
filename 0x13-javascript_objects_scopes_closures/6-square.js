#!/usr/bin/node
const BaseSquare = require('./5-square');

class Square extends BaseSquare {
  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) process.stdout.write(c);
        console.log();
      }
    } else super.print();
  }
}
module.exports = Square;
