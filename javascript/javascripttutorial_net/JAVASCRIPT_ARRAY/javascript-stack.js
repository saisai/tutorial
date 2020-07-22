
let stack = [];

stack.push(1);
console.log(stack);


stack.push(2);
console.log(stack);


stack.push('hello');
console.log(stack);

let hello = () => "hello world";

stack.push(hello)
console.log(stack);


let person = {
    name: "Jone doe",
    age: 30,
    location: "London"
};

stack.push(person);
console.log(stack);

class Car {

    constructor(model, color){
        this.model = model;
        this.color = color;
    }

    get()
    {
        return this.model +' '+ this.color;
    }

}

car = new Car("002", "red");
stack.push(car)

console.log(stack);

console.log(stack.length);

while(stack.length > 0) {
    let result = stack.pop();
    console.log(typeof result);

}

console.log(stack.length);


function reverse(str) {

    let stack = [];

    // push letter into stack
    for (let i=0; i < str.length; i++) {
        stack.push(str[i]);
    }

    // pop letter from the stack
    let reverseStr = '';
    while (stack.length > 0) {
        reverseStr += stack.pop();
    }

    return reverseStr;
}
console.log(reverse("Javascript Stack"));
