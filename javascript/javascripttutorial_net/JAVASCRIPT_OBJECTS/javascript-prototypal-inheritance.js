let animal = {
    walk: function() {
        console.log("walking");
    }
};

let bird = {
    fly: function() {
        console.log('flying');
    }
}

bird.__proto__ = animal;

bird.walk();
bird.fly();

