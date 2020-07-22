function Animal(name) {
    this.name = name;
}

Animal.prototype.identify = function() {
    console.log("I'm " + this.name);
}

var donald = new Animal("Donald");
donald.identify();


var bob = new Animal("Bob");
bob.identify();

