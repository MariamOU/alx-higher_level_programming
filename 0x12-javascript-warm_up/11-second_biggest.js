#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const arg = process.argv.slice(2).map(parseInt);
  const argg = arg.sort(function (a, b) { return b - a; })[1];
  console.log(argg);
}
