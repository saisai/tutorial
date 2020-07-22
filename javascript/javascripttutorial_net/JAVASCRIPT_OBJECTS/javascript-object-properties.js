let person = {};

person.age = 25;

delete person.age;

console.log(person.age);


'use strict';

let person2 = {};

Object.defineProperty(person2, 'ssn', {
    configurable: false,
    value: '012-38-9119'
});

delete person2.ssn;


/*
Object.defineProperty(person2, 'ssn', {
    configurable: true
});
*/

let person3 = {};
person3.age = 25;
person3.ssn = '012-35-6986';

for(let prop in person3) {
    console.log(prop)
}


Object.defineProperty(person3, 'ssn', {
    enumerable: false
});

for(let prop in person3) {
    console.log(prop);
}



let person4 = {
    firstName: "John",
    lastName: "Doe"
}

Object.defineProperty(person4, 'fullName', {
    get: function() {
        return this.firstName + ' ' + this.lastName;
    },

    set: function(value) {

        let parts = value.split(' ');
        if(parts.length == 2) {
            this.firstName = parts[0];
            this.lastName = parts[1];
        }else {
            throw 'Invalid naem format';
        }

    }
});

console.log(person4.fullName);


var product = {};

Object.defineProperties(product, {
    name: {
        value: "Smartphone"
    },
    price: {
        value: 799
    },
    tax : {
        value: 0.1
    },
    netPrice: {
        get: function() {
            return this.price * (1 + this.tax);
        }
    }
});

console.log('The net price of a ' + product.name + ' is ' + product.netPrice.toFixed(2) + ' USD');



let person5 = {
    firstName: "John",
    lastName: "Doe"
};

let descriptor = Object.getOwnPropertyDescriptor(person5, 'firstName');

console.log(descriptor);


