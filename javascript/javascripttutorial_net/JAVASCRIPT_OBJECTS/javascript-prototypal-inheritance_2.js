var animal = {
    legs: 4,
    walk: function() {
        console.log('walking on ' + this.legs + ' legs');
    }
}

var bird = {
    legs: 2,
    fly: function() {
        console.log('flying');
    }
}

bird.__proto__ = animal;

bird.walk();

