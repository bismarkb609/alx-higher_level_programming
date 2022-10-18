#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2];

fs.readMe(file, 'utf8', function (err, data) {
  console.error('error', err);
  console.log(data);
});
