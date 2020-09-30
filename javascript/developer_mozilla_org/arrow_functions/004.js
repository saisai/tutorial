
var func = x => x * x;

console.log(func(2));


var funa = (x, y) => x * y;


console.log(funa(3, 4));

var funb = (x, y) => { return x + y; };


console.log(funb(3, 4));


var func = () => {foo: 1};

console.log(func());

var fund = () => ( {foo: 1});

console.log(fund());

