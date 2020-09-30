let add = function(x, y) {
    return x + y;
}

console.log(add(10, 30));

let adda = (x, y) => x + y;

console.log(adda(10, 30));

let addb = (x, y) => { return x + y; };

console.log(addb(10, 30));


let numbers = [2, 3, 4];
numbers.sort(function(a, b){
    return b - a;
});
console.log(numbers);


let numbers2 = [2, 3, 4];
numbers2.sort((a, b) => b - a);

console.log(numbers2);

let names = ['John', 'Mac', 'Peter'];
let lengths = names.map(name => name.length);
console.log(lengths);

