const counter = {
    count: 0,
    next: function() {
        return ++this.count;
    }
};

console.log(counter.next());
console.log(counter.next());
console.log(counter.next());


/*
function show() {
    console.log(this === window);
}

show();
*/
function getBrand(prefix) {
    console.log(prefix + this.brand);
}

let honda = {
    brand: "Honda"
};

let audi = {
    brand: "Audi"
};

getBrand.call(honda, "It's a");
getBrand.call(audi, "It's a");


getBrand.apply(honda, ["It's a "]);
getBrand.apply(audi, ["It's an "]);

