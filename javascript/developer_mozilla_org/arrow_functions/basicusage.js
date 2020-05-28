// an empty arrow function returns undefined

let empty = () => {};

console.log(empty());


let result = (() => 'foobar')();
console.log(result);
// Returns "foobar"
// (this is an Immediately Invoked Function Expression)

var simple = a => a > 15 ? 15 : a;
console.log(simple(16));
console.log(simple(10));

let max = (a, b) => a > b ? a : b;

console.log(max(3, 4));
