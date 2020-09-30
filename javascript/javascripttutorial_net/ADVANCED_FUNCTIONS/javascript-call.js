function show() {

}

console.log(show instanceof Function);

function show() {
    console.log("Show function");
}

show();

show.call();


function add(a, b) {
    return a + b;
}

let result = add.call(this, 10, 20);
console.log(result);


const car = {
    name: "car",
    start: function() {
        console.log("Start the " + this.name);
    },
    speedup: function() {
        console.log("Speed up the "+ this.name)
    },
    stop: function() {
        console.log("Stop the "+ this.name);
    }
};


const aircraft = {
    name: "aircraft",
    fly: function() {
        console.log("Fly");
    }
};

car.start.call(aircraft);
