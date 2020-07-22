let numbers = [1, 3, 5];

let result = true;

for(let i=0; i < numbers.length; i++) {
    if(numbers[i] <= 0) {
        result = false;
        break;
    }
}

console.log(result);


console.log(numbers);

let result1 = numbers.every(function(e) {
    return e > 0;
});

console.log(result1);

let resulta = numbers.every( e =>  e > 0 );

console.log(resulta);


let isEven = numbers.every( e => e % 2 == 0 );

console.log(isEven);

