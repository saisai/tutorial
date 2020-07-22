var animal = {
    legs: 4,
    walk: function() {
        console.log('walking on ' + this.legs + ' legs');
    }
}

let bird = Object.create(animal);

console.log(bird.prototype === animal.prototype);

bird.legs = 2;
bird.fly = function() {
    console.log('flying');
}

bird.fly();



