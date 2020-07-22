console.log(Object);
console.log(Object.prototype);


function Foo(name) {
    this.name = name;
};

console.log(Foo);
console.log(Foo.prototype);

Foo.prototype.whoAmI = function() {
    return "I am " + this.name;
}

let a = new Foo("a");

let b = new Foo('b');


b.say = function() {
    console.log("Hi from " + this.whoAmI());
}

console.log(a.constructor);


console.log(a.constructor === Foo);


console.log(a.__proto__ === Object.getPrototypeOf(a));

console.log(a.constructor.prototype);

console.log(a.whoAmI());


a.whoAmI = function() {
    console.log("This is " + this.name);
}

console.log(a.whoAmI());

