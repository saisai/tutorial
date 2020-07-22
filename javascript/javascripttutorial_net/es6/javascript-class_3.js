let Animal = class {
    constructor(type) {
        this.type =type;
    }

    identify() {
        console.log(this.type);
    }
}


let duck = new Animal("Duck");

console.log(duck instanceof Animal);
console.log(duck instanceof Object);


console.log(typeof Animal);
console.log(typeof Animal.prototype);

