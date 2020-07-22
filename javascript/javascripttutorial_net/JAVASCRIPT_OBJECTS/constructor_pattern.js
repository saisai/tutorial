function Animal(name) {

    this.name = name;
    this.identify = function() {
        console.log("I'm " + this.name);
    }
}
var donald = new Animal("Donald");

console.log(donald.identify());

console.log(donald.constructor === Animal);
console.log(donald instanceof Animal);
console.log(donald instanceof Object);

