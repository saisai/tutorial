let empty = () => {};

console.log(empty);
console.log(empty());


let result = (() => 'foobar')();

console.log(result);

//let test = ( function () {return 'foobar';} )();
let test = ( function () {
        return ['a', 1, 3, 'b'];
} )();

console.log(test);


let tt = ( () =>
    ({ foo: 1, bar: 2})
)();
// this is an Immediately Invoked Function Expression

console.log(tt);
console.log(typeof tt);

Object.keys(tt).forEach(function(key) {

    console.log(key, tt[key]);
})

Object.keys(tt).forEach(  key => console.log(key, tt[key]) );


var simple = a => a > 15 ? 15 : a;
console.log(simple(15));
console.log(simple(10));


var simplef = function(a) { return a > 15 ? 15 : a; };

console.log(simplef(10));
console.log(simplef(16));


let max = (a, b) => a > b ? a : b;

console.log(max(3, 4));


let maxf = function(a, b) { return a > b ? a : b; };

console.log(maxf(5, 4));


// easy array filtering, mapping, ...

var arr = [5, 6, 13, 0, 1, 18, 23];

var sum = arr.reduce((a, b) => a + b);

console.log(sum);

var sumf = arr.reduce( function(a, b) { return a + b; } );

console.log(sumf);

var even = arr.filter(v => v % 2 == 0);
console.log(even);

var evenf = arr.filter(function(v) { return v %2 == 0; })

console.log(evenf);


var double = arr.map(v => v * 2);
console.log(double);

var doublef = arr.map(function(v) { return v *2; });

console.log(doublef);


// Parameterless arrow functions that are visually easier to parse
setTimeout( () => {
    console.log("I happen sooner");
    setTimeout( () => {
        // deeper code
        console.log("I happern later");
    }, 1);
}, 1);


setTimeout( function() {
    console.log("Function happen sooner");
    setTimeout( function() {
        // deeper code
        console.log("Function happern later");
    }, 5 );
    setTimeout( function() {
        // deeper code
        console.log("Function happern between");
    }, 6 );	

}, 3);
