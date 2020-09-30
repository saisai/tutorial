var func = () => {foo: 1};
console.log(func)
console.log(func())

// SyntaxError
//var func2 = () => { foo: function() {}};

//console.log(func2);


var func3 = () => ({ foo: 1 });

console.log(func3())
