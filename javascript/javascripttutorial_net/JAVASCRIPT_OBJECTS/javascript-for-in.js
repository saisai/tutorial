
var person = {
    firstName: "John",
    lastName: "Doe",
    ssn: "122-22-3333"
};

for(var prop in person) {
    console.log(prop + " " + person[prop]);
}


var decoration = {
    color: "red"
};

var circle = Object.create(decoration);
circle.radius = 10;

for(const prop in circle) {
    console.log(prop);
}


const items = [10 , 20, 30];
let total = 0;

Array.prototype.foo = 100;

for(const item in items) {
    total += items[item];
}
console.log(total);


var arr = [];
// set the third element to 3, other elements are `undefined`
arr[2] = 3;

for (let i = 0; i < arr.length; i++) {
    console.log(arr[i]);
}


for (const key in arr) {
    console.log(arr[key]);
}
