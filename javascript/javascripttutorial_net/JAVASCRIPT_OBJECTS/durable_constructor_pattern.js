function secureAnimal(name) {

    var o = new Object();

    o.identify = function() {
        console.log(name); // no this
    }

    return o;
}

var alien = secureAnimal("?#@");
alien.identify();

