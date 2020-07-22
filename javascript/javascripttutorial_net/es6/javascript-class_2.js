class Animal {
    constructor(type) {
        this.type = type;
    }

    identify() {
        console.log(this.type);
    }
}

let cat = new Animal("Cat");
cat.identify();

console.log(typeof Animal);
