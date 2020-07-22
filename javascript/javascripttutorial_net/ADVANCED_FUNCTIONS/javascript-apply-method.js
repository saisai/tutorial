const person = {
    firstName: "John",
    lastName: "Doe"
};

function greet(greeting, message) {
    return `${greeting} ${this.firstName}. ${message}`;
}


let result =greet.apply(person, ['Hello', "How are you?"]);
console.log(result);

let resultcall = greet.call(person, "hello", "How are you?");

console.log(resultcall);


const computer = {
    name: 'MacBook',
    isOn: false,
    turnOn() {
        this.isOn = true;
        return `The ${this.name} is On`;
    },
    turnOff() {
        this.isOn = false;
        return `The ${this.name} is Off`;
    }
};

const server = {
    name: "Dell PowerEdge T30",
    isOn: false
};

let resulton = computer.turnOn.apply(server);
console.log(resulton);

let resultoff = computer.turnOff.apply(server);

console.log(resultoff);


let arr = [1, 2, 3];
let numbers = [4, 5, 6];

arr.push.apply(arr, numbers);

console.log(arr);
console.log(numbers);

console.log(JSON.stringify(arr));
let json = JSON.stringify(arr);
console.log(typeof json);
console.log(JSON.parse(json));
let jsonobj = JSON.parse(json);
console.log(typeof jsonobj);

console.log("Check if the object is array or obj " +Array.isArray(jsonobj));

console.log( Object.prototype.toString.call(jsonobj));
console.log( Object.prototype.toString.call(json));
