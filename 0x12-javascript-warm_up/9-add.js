#!/usr/bin/node
function add (a, b) {
  const x = a + b;
  console.log(x);
}
add(parseInt(process.argv[2]), parseInt(process.argv[3]));
