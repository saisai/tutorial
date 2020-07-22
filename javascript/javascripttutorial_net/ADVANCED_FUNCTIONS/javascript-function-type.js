function swap(x, y) {
    let tmp = x;
    x = y;
    y = tmp;
}

console.log(swap.length);
console.log(swap.prototype);

function fn() {
    console.log(new.target);
}

fn(); // undefined
let f = new fn(); // [Function: fn]


let cat = {type: "Cat", sound: "Meow"};
let dog = {type: "Dog", sound: "Woof"};

let say = function(greeting) {
    console.log(greeting);
    // access current this
    console.log(this.type + " says " + this.sound);
}

say.apply(cat, ['Hi']);
say.apply(dog, ['Hi']);


say.call(cat, 'Hi');
say.call(dog, 'Hi');

let car = {
    speed: 5,
    start: function() {
        console.log("Starts with " + this.speed + " km/h");
    }
};

let aircraft = {
    speed: 10,
    fly: function() {
        console.log("Flying");
    }
};

let taxiing = car.start.bind(aircraft);

taxiing();

car.start.call(aircraft);

