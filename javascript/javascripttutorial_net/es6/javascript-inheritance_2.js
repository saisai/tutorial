class Animal{
    constructor(legs) {
        this.legs = legs;
    }
    walk() {
        console.log("walking on " + this.legs + " legs");
    }
}

class Bird extends Animal {

    constructor(legs, color) {
        super(legs);
        this.color = color;

    }

    fly() {

        console.log("flying");
    }

    getColor() {
        console.log(this.color);
    }
}

let bird = new Bird(2, 'white');

bird.walk();
bird.fly();
bird.getColor();

