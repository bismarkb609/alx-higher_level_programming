#!/usr/bin/node

const args = process.argv[2];
let is_number = typeof Number(args) === "number";

if (is_number) {
  console.log('My number: ' + Number(args));
} else {
  console.log('Not a number');
}
