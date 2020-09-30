
function object(o) {
    function F() {};
    F.prototype = o;
    return new F();
}

var animal = {
    legs: 4,
    walk: function() {
        console.log('walking on ' + this.legs + ' legs');
    }
}

var bird = object(animal);

bird.legs = 2;
bird.fly = function() {
    console.log('flying');
}

bird.walk(); // walking on 2 legs
bird.fly(); // flying
